# Gemini Context & Rules: UXAgent Frontend AI Assistant

Esta configuración incorpora y activa oficialmente el agente frontend y sus directivas de arquitectura, accesibilidad y diseño en Gemini.

## Agente Orquestador Principal

@[UXAGENT.md](./UXAGENT.md)

## Resumen Operativo para Gemini

- **Protocolo Obligatorio (Fases 0 a 4):** Sigue estrictamente las fases de ejecución de [`./UXAGENT.md`](./UXAGENT.md) antes de modificar o generar código frontend.
- **Tokens y Diseño:** La fuente de verdad visual es [`./DESIGN.md`](./DESIGN.md) (espacio perceptualmente uniforme OKLCH, escala fluida `clamp()`, retícula de 4px y áreas táctiles de 44x44px).
- **Skills Especializadas:** Activa de forma progresiva las skills ubicadas en [`./skills/`](./skills/):
  - [`./skills/brand-identity-discovery/SKILL.md`](./skills/brand-identity-discovery/SKILL.md): Auditoría de marca y generación de tokens iniciales.
  - [`./skills/framework-token-adapter/SKILL.md`](./skills/framework-token-adapter/SKILL.md): Inyección de tokens en Tailwind v3/v4 o CSS Modules.
  - [`./skills/design-system-auditor/SKILL.md`](./skills/design-system-auditor/SKILL.md): Reutilización sobre creación y auditoría de UI.
  - [`./skills/writing-ui-components/SKILL.md`](./skills/writing-ui-components/SKILL.md): Estructura, abstracción y 3 estados obligatorios (Cargando, Vacío, Error).
  - [`./skills/accessibility-contrast-auditor/SKILL.md`](./skills/accessibility-contrast-auditor/SKILL.md): Contraste mínimo WCAG y hitboxes accesibles.
