# Spec: Molecule — Infinite Marquee / Ticker Strip (`molecule-marquee`)

Banda cinética horizontal de desplazamiento continuo para titulares de marca, anuncios o separación expresiva entre secciones.

---

## 1. 🎯 Fingerprint & Heuristic Matching

- **Selectores Semánticos / Estructurales:** `<section>` o `<div>` con `overflow: hidden` y `white-space: nowrap` que contiene dos pistas gemelas (`display: flex`) animadas mediante `translateX(-50%)` en bucle continuo.
- **Heurística de Caja (Playwright):**
  - Ancho completo o desbordado (`width >= 100vw`, ej. `106%` con rotación ligera `-2deg` / `2deg`), bordes superior e inferior gruesos (`border-y: 4px` a `8px`) y sombra dura.
  - Cuando es puramente decorativo o repite el nombre de la marca, lleva `aria-hidden="true"` en el contenedor raíz.

---

## 2. 📐 Component Interface & Props

```typescript
export interface MarqueeProps {
  /** Texto o elementos repetidos a lo largo de la cinta */
  items: string[];
  /** Duración de un ciclo completo en segundos (por defecto 20s) */
  durationSeconds?: number;
  /** Dirección del desplazamiento horizontal */
  direction?: 'left' | 'right';
  /** Si el contenido es decorativo (oculta la repetición a lectores de pantalla) */
  decorative?: boolean;
  /** Pausar animación al posar el cursor o enfocar */
  pauseOnHover?: boolean;
}
```

### Mapeo a Tokens de `./DESIGN.md`
- **Superficie:** `--color-primary` (`oklch(0.64 0.24 31)`) o `--color-secondary` con texto en alto contraste.
- **Bordes:** `4px` a `8px solid var(--color-on-surface)` y sombra dura `0 8px 0 0 var(--color-on-surface)`.

---

## 3. ♿ Reglas de Accesibilidad (a11y) & Estados

- **Movimiento Reducido (WCAG 2.3.3 / 2.2.2):**
  - Bajo `@media (prefers-reduced-motion: reduce)`, la animación `marquee` debe desactivarse (`animation: none !important`), mostrando una sola pista estática legible sin recorte crítico.
- **Lectores de Pantalla:**
  - Si es un separador de marca repetitivo (`"BRAVODESIGN BRAVODESIGN..."`), el contenedor raíz lleva `aria-hidden="true"`.
  - Si contiene avisos informativos reales, solo la primera pista es visible para el árbol de accesibilidad y la pista duplicada lleva `aria-hidden="true"`.
