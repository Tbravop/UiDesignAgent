---
name: design-system-auditor
description: Disparar al auditar un sitio o repositorio con Playwright y antes de crear, modificar o estandarizar cualquier vista o componente UI (Regla 1 de UXAGENT.md). Realiza un escaneo exhaustivo y recursivo de todas las vistas, páginas y rutas del proyecto sin importar su nivel de anidamiento, prioriza la biblioteca nativa del proyecto, estandariza y corrige activamente problemas de contraste, tamaños de texto dispersos y clases duplicadas para cajas iguales en las vistas, y usa ./specs/ para componentes más abstractos o inexistentes en la biblioteca.
---

# Design System Auditor Skill (Active Standardization, Library-First & Playwright Engine)

Esta skill gobierna el rol principal del agente al auditar y mejorar cualquier proyecto frontend (`Vue.js`, `Angular`, `React`, `Svelte`, `HTML + Utility CSS`, etc.):
0. **Descubrimiento y Mapeo Recursivo de Vistas (`Deep View Discovery`):** Localiza y cataloga exhaustivamente **todas las vistas, rutas y páginas del proyecto**, sin importar cuán anidadas estén o en qué subcarpetas residan (monorepos, sub-módulos, dominios de negocio o subrutas).
1. **Prioridad de Biblioteca Nativa (`Library-First Priority`):** Si el proyecto utiliza una biblioteca de UI o CSS, todo componente estándar actual o futuro se mantiene y construye directamente con esa biblioteca.
2. **Estandarización, Corrección y Optimización Activa de Vistas (`Active View Standardization`):** El agente utiliza **Playwright** junto con [`DESIGN.md`](../../DESIGN.md) y `./specs/` para detectar y **corregir directamente en la vista** problemas de diseño, usabilidad y accesibilidad:
   - **Mal contraste entre botones, badges o textos (WCAG AA `< 4.5:1`).**
   - **2 clases distintas para 2 cajas iguales** (ej. sombras hardcodeadas dispares, paddings o bordes inconsistentes en elementos hermanos).
   - **Exceso de variables de tamaño de texto o fuentes mezcladas** para el mismo rol jerárquico.
   - **Hitboxes táctiles insuficientes (`< 44x44px`) y falta de `prefers-reduced-motion`.**
3. **Uso Específico de `./specs/` para Componentes Abstractos o Distintos:** Cuando el usuario busca crear un componente más **abstracto, distinto o que la biblioteca nativa no posee**, el agente consulta (o auto-genera si falta) su `.spec.md` en `./specs/` y lo construye en `./src/components/`.

---

## 1. Descubrimiento Exhaustivo y Recursivo de Vistas (Deep View Discovery)

Para comenzar cualquier proyecto o auditoría de la mejor manera, el agente **nunca debe asumir una sola carpeta superficial** ni pasar por alto vistas dentro de subdirectorios profundos.

### Heurísticas de Detección Recursiva por Arquitectura:
- **Enrutadores basados en sistema de archivos (File-based Routing):**
  - **Next.js App Router:** Rastreo recursivo en `app/**/page.{tsx,jsx,js}` o `src/app/**/page.{tsx,jsx,js}`.
  - **Next.js Pages / Nuxt / SvelteKit / Astro:** Rastreo recursivo en `pages/**/*.{tsx,jsx,vue,svelte,astro}` o `src/pages/**`, `routes/**/+page.svelte`.
- **Enrutadores Declarativos / SPA Clásica (React Router, Vue Router, Angular Router):**
  - Rastreo en carpetas de vistas principales y anidadas: `**/views/**/*.{vue,tsx,jsx,html}`, `**/pages/**/*.{vue,tsx,jsx}`, `**/scenes/**/*.{tsx,jsx}`, `**/screens/**/*.{tsx,jsx}`.
  - Rastreo en arquitecturas basadas en dominio (*Feature-based* o *Domain-Driven*): `src/features/**/pages/`, `src/features/**/components/*Page.tsx`, `src/modules/**/views/`, `src/domains/**/screens/`.
  - Análisis del árbol de rutas: Inspeccionar recursivamente `routes.ts`, `router.js`, `AppRoutes.tsx`, `router/index.ts` o `app-routing.module.ts` para mapear los componentes asociados a cada `path`.
- **Plantillas HTML / SSR / Multi-page tradicionales:**
  - Rastreo recursivo de todas las plantillas y vistas HTML: `**/templates/**/*.html`, `**/views/**/*.html`, `**/templates/**/*.jinja2`, `public/**/*.html`.

### Regla de Rastreo Desatendido:
El agente ejecuta comandos de búsqueda profunda (ej. en PowerShell: `Get-ChildItem -Recurse -File -Include *page*, *view*, *screen*, *.html`) para inventariar todas las pantallas antes de proceder a la Fase 1.

---

## 2. Árbol de Decisión: Biblioteca Nativa vs. `./specs/` vs. Estandarización de Vista

```
         [Auditoría en Vivo de la Vista con Playwright]
                                │
   ┌────────────────────────────┴────────────────────────────┐
   ▼                                                         ▼
[Elementos que YA existen en la Vista]        [Solicitud de Nuevo Componente]
   │                                                         │
   ▼                                          ¿Existe en la biblioteca nativa?
¿Tienen mal contraste (< 4.5:1),                             │
2 clases distintas para cajas iguales,            ┌──────────┴──────────┐
tamaños de texto dispersos o hitbox < 44px?       ▼                     ▼
   │                                            [SÍ]                  [NO / Es más abstracto
   ▼                                              │                    o distinto]
[ESTANDARIZAR Y ARREGLAR EN LA VISTA]             ▼                     │
• Mantener la biblioteca del proyecto          [Usar la biblioteca      ▼
• Unificar clases en cajas hermanas             nativa aplicando     [Entra ./specs/:
• Corregir contraste OKLCH / WCAG AA            tokens y reglas de    Consultar o crear .spec.md
• Normalizar escala de tamaños de texto         accesibilidad]        y construir en ./src/components/]
• Garantizar hitbox >= 44px
```

---

## 2. Protocolo de Estandarización Activa sobre las Vistas (4 Reglas de Corrección)

Cuando `/design-system-auditor` analiza una página con Playwright, **no deja la vista con errores**: interviene sobre el archivo de la vista para estandarizar, arreglar, optimizar y mejorar:

### A. Corrección de Contraste entre Botones, Badges y Superficies (WCAG 2.1 AA)
- Calcular la luminancia relativa real (`window.getComputedStyle(el).backgroundColor` vs `color`) en cada botón, badge, chip y enlace.
- Si el contraste es `< 4.5:1` en texto normal (ej. texto blanco `#ffffff` sobre naranja `#ff4f00` = `3.29:1`), corregir inmediatamente en la vista usando el par de alto contraste del sistema (ej. `text-on-surface` `#1c1b1b` sobre `#ff4f00` = `5.17:1`) o ajustando el token según [`DESIGN.md`](../../DESIGN.md).

### B. Unificación de Cajas Iguales ("Prohibido 2 Clases Distintas para 2 Cajas Iguales")
- Si dos o más elementos cumplen el mismo rol estructural (ej. tarjetas de proyecto hermanas, lista de chips de habilidades, botones de acción secundarios), **deben compartir exactamente las mismas clases de borde, sombra, radio, padding y transición**.
- Eliminar valores arbitrarios hardcodeados en línea (ej. mezclar `shadow-[4px_4px_0px_0px_#000]`, `shadow-[4px_4px_0px_0px_#1c1b1b]` y `shadow-[4px_4px_0px_0px_#56589a]`) y estandarizarlos a la clase o token oficial del proyecto (ej. `.neo-shadow-sm` o `.neo-shadow`).

### C. Normalización de Variables de Tamaño de Texto y Familias Tipográficas
- Auditar que no existan múltiples clases de fuente o tamaños dispares para el mismo nivel semántico (ej. mezclar `font-mono` y `font-label-mono`, o usar 5 tamaños distintos de texto para botones del mismo nivel).
- Estandarizar los elementos equivalentes a una escala tipográfica coherente y acotada definida en [`DESIGN.md`](../../DESIGN.md).

### D. Usabilidad Táctil y Movimiento Reducido
- Todo elemento interactivo (`<a>`, `<button>`, `[role="button"]`) debe medir al menos `44x44px` en el DOM renderizado (`min-h-[44px] inline-flex items-center`).
- Garantizar siempre la presencia de `@media (prefers-reduced-motion: reduce)` para pausar animaciones infinitas o desplazamientos bruscos.

---

## 3. Cuándo Crear o Usar `./specs/` (Componentes Abstractos o Faltantes)

1. **Referencia de Estándares:** Durante la auditoría de una vista hecha con cualquier biblioteca, `./specs/` sirve como contrato de referencia para saber qué exige cada patrón (contraste, ARIA, hitbox, anatomía).
2. **Creación de Componentes Más Abstractos o Distintos:** Si el usuario necesita un componente que no existe en la biblioteca o que requiere una abstracción especial (ej. `ai-decomposition-tree`, `otp-input`, `command-palette`, `data-table-slicer`), el agente usa `./specs/` (o auto-genera el `.spec.md` faltante si descubre un patrón nuevo con Playwright) y construye el componente modular en `./src/components/` adaptado al framework del proyecto (`Vue`, `Angular`, `React`, `Svelte` o `HTML`).

---

## Lista de Verificación de `/design-system-auditor`

- [ ] Se ejecutó el mapeo recursivo profundo descubriendo todas las vistas en cualquier nivel de anidamiento (`app/**`, `pages/**`, `features/**`, `templates/**`, etc.).
- [ ] Se respetó la biblioteca nativa del proyecto sin reemplazarla innecesariamente.
- [ ] Se corrigieron en la vista todos los problemas de contraste `< 4.5:1` en botones, badges y chips.
- [ ] Se unificaron las clases de todas las cajas iguales (cero sombras o paddings dispares entre elementos hermanos).
- [ ] Se normalizaron las variables de tamaño de texto y familias de fuente (`font-label-mono`, `font-display`, `font-body-md`).
- [ ] Todos los controles interactivos cumplen con `height >= 44px` y existe soporte `@media (prefers-reduced-motion: reduce)`.
