import json
import sys
import threading
import functools
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from playwright.sync_api import sync_playwright

sys.stdout.reconfigure(encoding="utf-8")


def start_temp_server(root_dir: Path, port: int = 8123):
    handler = functools.partial(SimpleHTTPRequestHandler, directory=str(root_dir))
    server = HTTPServer(("127.0.0.1", port), handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    return server


def run_audit():
    root_dir = Path(__file__).resolve().parent.parent
    server = start_temp_server(root_dir, 8123)

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page(viewport={"width": 1440, "height": 900})

            print("--> Ejecutando auditoría de Estandarización, Contraste y Accesibilidad con Playwright...")
            page.goto("http://127.0.0.1:8123/index.html", wait_until="networkidle")

            audit_results = page.evaluate("""() => {
                // Función auxiliar para calcular ratio de contraste WCAG 2.1
                const parseRgb = (str) => {
                    const m = str.match(/rgba?\\((\\d+),\\s*(\\d+),\\s*(\\d+)/);
                    return m ? [Number(m[1]), Number(m[2]), Number(m[3])] : [255, 255, 255];
                };
                const luminance = ([r, g, b]) => {
                    const a = [r, g, b].map(v => {
                        v /= 255;
                        return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4);
                    });
                    return a[0] * 0.2126 + a[1] * 0.7152 + a[2] * 0.0722;
                };
                const contrastRatio = (fgStr, bgStr) => {
                    const l1 = luminance(parseRgb(fgStr));
                    const l2 = luminance(parseRgb(bgStr));
                    const brightest = Math.max(l1, l2);
                    const darkest = Math.min(l1, l2);
                    return Number(((brightest + 0.05) / (darkest + 0.05)).toFixed(2));
                };

                // 1. Auditar los 11 chips de #skills (Igualdad de Cajas + Contraste + Hitbox)
                const skillItems = Array.from(document.querySelectorAll('#skills ul li')).map(li => {
                    const s = window.getComputedStyle(li);
                    const r = li.getBoundingClientRect();
                    const ratio = contrastRatio(s.color, s.backgroundColor);
                    return {
                        text: li.innerText.trim(),
                        boxShadow: s.boxShadow,
                        borderWidth: s.borderWidth,
                        height: Math.round(r.height),
                        contrastRatio: ratio,
                        passesWCAG_AA: ratio >= 4.5,
                        hasStandardShadowClass: li.classList.contains('neo-shadow-sm'),
                        hasStandardHoverClass: li.classList.contains('neo-hover')
                    };
                });

                const uniqueChipShadows = Array.from(new Set(skillItems.map(i => i.boxShadow)));

                // 2. Auditar botones del Header y enlaces de acción en #work
                const interactiveControls = Array.from(
                    document.querySelectorAll('header nav a, #work article a')
                ).map(a => {
                    const s = window.getComputedStyle(a);
                    const r = a.getBoundingClientRect();
                    return {
                        text: a.innerText.trim(),
                        height: Math.round(r.height),
                        meetsMinHitbox44px: Math.round(r.height) >= 44
                    };
                });

                // 3. Auditar consistencia de las 3 tarjetas de #work
                const workCards = Array.from(document.querySelectorAll('#work article')).map(art => {
                    const offsetLayer = art.firstElementChild;
                    const badge = art.querySelector('span');
                    const bs = badge ? window.getComputedStyle(badge) : null;
                    const bRatio = bs ? contrastRatio(bs.color, bs.backgroundColor) : 0;
                    return {
                        title: art.querySelector('h3')?.innerText.trim(),
                        shadowOffsetClasses: offsetLayer ? offsetLayer.className : '',
                        badgeContrastRatio: bRatio,
                        badgePassesWCAG_AA: bRatio >= 4.5
                    };
                });

                // 4. Auditar unificación tipográfica (0 font-mono huérfanos)
                const unstandardizedFontMonoCount = document.querySelectorAll('.font-mono').length;

                return {
                    libraryDetected: 'Tailwind CSS (Library-First Preserved)',
                    skillsChipsAudit: {
                        totalChips: skillItems.length,
                        allUseSameShadow: uniqueChipShadows.length === 1,
                        uniqueShadowValues: uniqueChipShadows,
                        allPassWCAG_AA: skillItems.every(i => i.passesWCAG_AA),
                        allMeetHitbox44px: skillItems.every(i => i.height >= 44),
                        sampleChips: skillItems.slice(0, 3).concat(skillItems.slice(-1))
                    },
                    workCardsAudit: {
                        allBadgesPassWCAG_AA: workCards.every(c => c.badgePassesWCAG_AA),
                        cards: workCards
                    },
                    interactiveHitboxesAudit: {
                        totalChecked: interactiveControls.length,
                        allMeet44px: interactiveControls.every(c => c.meetsMinHitbox44px),
                        controls: interactiveControls
                    },
                    typographyStandardization: {
                        legacyFontMonoOccurrences: unstandardizedFontMonoCount,
                        status: unstandardizedFontMonoCount === 0 ? 'UNIFIED_TO_FONT_LABEL_MONO' : 'NEEDS_CLEANUP'
                    }
                };
            }""")

            print("=== REPORTE DE ESTANDARIZACIÓN Y ACCESIBILIDAD EN VIVO (PLAYWRIGHT) ===")
            print(json.dumps(audit_results, indent=2, ensure_ascii=False))
            browser.close()
    finally:
        server.shutdown()


if __name__ == "__main__":
    run_audit()
