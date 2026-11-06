# Gemini Context & Rules: UXAgent Frontend AI Assistant

Esta configuración incorpora y activa oficialmente el agente frontend y sus directivas de arquitectura, accesibilidad y diseño en Gemini.

## Agente Orquestador Principal

@[UXAGENT.md](./UXAGENT.md)

## Resumen Operativo para Gemini

- **Protocolo Obligatorio (Fases 0 a 4):** Sigue estrictamente las fases de ejecución de [`./UXAGENT.md`](./UXAGENT.md) antes de modificar o generar código frontend.
- **Tokens y Diseño:** La fuente de verdad visual es [`./DESIGN.md`](./DESIGN.md) (espacio perceptualmente uniforme OKLCH, escala fluida `clamp()`, retícula de 4px y áreas táctiles de 44x44px).
- **Skills Especializadas:** Cada skill reside en su propio directorio dentro de [`./skills/`](./skills/) con su punto de entrada `skill.md`:
  - [`./skills/brand-identity-discovery/skill.md`](./skills/brand-identity-discovery/skill.md): Auditoría de marca y generación de tokens iniciales.
  - [`./skills/framework-token-adapter/skill.md`](./skills/framework-token-adapter/skill.md): Inyección de tokens en Tailwind v3/v4 o CSS Modules.
  - [`./skills/design-system-auditor/skill.md`](./skills/design-system-auditor/skill.md): Reutilización sobre creación y auditoría de UI.
  - [`./skills/writing-ui-components/skill.md`](./skills/writing-ui-components/skill.md): Estructura, abstracción y 3 estados obligatorios (Cargando, Vacío, Error).
  - [`./skills/accessibility-contrast-auditor/skill.md`](./skills/accessibility-contrast-auditor/skill.md): Contraste mínimo WCAG y hitboxes accesibles.
  - [`./skills/playwright-inspector/skill.md`](./skills/playwright-inspector/skill.md): Escaneo en vivo de DOM, extracción topológica computada y detección de clústeres.
  - [`./skills/ui-library-spec-extractor/skill.md`](./skills/ui-library-spec-extractor/skill.md): Extracción y generación en caliente de especificaciones `.spec.md`.
  - [`./skills/src-builder/skill.md`](./skills/src-builder/skill.md): Prioridad de biblioteca nativa vs construcción en `./src/components/`.
  - [`./skills/visual-clustering/skill.md`](./skills/visual-clustering/skill.md): Agrupamiento y extracción de propiedades visuales vía Playwright.
  - [`./skills/design-md-updater/skill.md`](./skills/design-md-updater/skill.md): Fusión y actualización de `DESIGN.md` preservando tokens de marca.
  - [`./skills/form-control-auditor/skill.md`](./skills/form-control-auditor/skill.md): Auditoría de controles de formulario y patrones WAI-ARIA.
  - [`./skills/github-route-resolver/skill.md`](./skills/github-route-resolver/skill.md): Compatibilidad de rutas POSIX relativas en GitHub.
  - [`./skills/layout-sorter/skill.md`](./skills/layout-sorter/skill.md): Estructuración semántica de contenedores DOM HTML5.
