# Spec: Atom — Separator / Divider (`atom-separator`)

Elemento estructural que divide semántica y visualmente secciones de contenido, grupos de listas o barras de herramientas.

---

## 1. 🎯 Fingerprint & Heuristic Matching

- **Selectores Semánticos / Estructurales:** `<hr>` nativo o `<div role="separator">`.
- **Heurística de Caja (Playwright):**
  - **Horizontal (`orientation="horizontal"`):** `width: 100%`, `height <= 4px` (o `border-top-width: 2px | 3px`).
  - **Vertical (`orientation="vertical"`):** `width <= 4px`, `align-self: stretch` o altura explícita dentro de un contenedor `display: flex`.

---

## 2. 📐 Component Interface & Props

```typescript
export interface SeparatorProps {
  /** Eje de división del contenedor */
  orientation?: 'horizontal' | 'vertical';
  /** Si es puramente visual, se marca como decorativo (aria-hidden="true") */
  decorative?: boolean;
  /** Variante de grosor y énfasis visual */
  variant?: 'solid' | 'dashed' | 'heavy';
  /** Etiqueta central opcional integrada en el divisor */
  label?: string;
}
```

### Mapeo a Tokens de `./DESIGN.md`
- **Trazo Base:** `--border-width-base` (`3px`) o `2px` en color `--color-on-surface` (`oklch(0.18 0.01 85)`).
- **Espaciado:** Múltiplos de la grilla de `4px` (`margin-block: 1.5rem` en horizontal; `margin-inline: 0.75rem` en vertical).

---

## 3. ♿ Reglas de Accesibilidad (a11y) & Estados

- **Rol Semántico:**
  - Cuando `decorative === true`, aplicar `role="none"` o `aria-hidden="true"`.
  - Cuando separa regiones semánticas relevantes, mantener `<hr>` o `role="separator"` con `aria-orientation="vertical"` si es vertical.
