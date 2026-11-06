# SPEC: AtomBadge (Badges, Status Indicators & Tags)

## 1. 🎯 Fingerprint & Heuristic Matching
- **DOM Signatures:**
  - Elementos `<span>`, `<div>` o `<label>` con texto corto en mayúsculas (1-4 palabras), `display: inline-flex | inline-block`, `font-size <= 12px`, padding compacto (`0.25rem 0.5rem` / `px-2 py-1`), borde visible (`border-2`) o fondo de color diferenciador.
  - Firmas de clases utilitarias de referencia: `.badge`, `.badge-primary`, `.badge-pill`, `.rounded-pill`.
  - En el portafolio: tags de categorías de proyectos (`bg-secondary text-white uppercase text-sm font-black tilt-left`).

## 2. 📐 Component Interface & Props
```typescript
export type BadgeVariant = 'primary' | 'secondary' | 'neutral' | 'success' | 'warning' | 'danger';
export type BadgeSize = 'sm' | 'md';

export interface BadgeProps extends React.HTMLAttributes<HTMLSpanElement> {
  variant?: BadgeVariant;
  size?: BadgeSize;
  isPill?: boolean;
  hasDot?: boolean;
  icon?: React.ReactNode;
  children: React.ReactNode;
}
```

## 3. ♿ Reglas de Accesibilidad (a11y) & Estados
- **Semántica:** Si el badge comunica un estado numérico o dinámico (ej. "3 mensajes nuevos"), debe incluir texto audible para lectores de pantalla vía `<span class="sr-only">`.
- **Contraste:** Todo badge con fondo de color debe garantizar un ratio de contraste mínimo de **4.5:1** (WCAG AA) para el texto interior (`oklch`).
- **Independencia del Color:** Los estados críticos (éxito, advertencia, error) no deben depender exclusivamente del color; deben reforzarse con un ícono descriptivo o etiqueta textual.
