# SPEC: MoleculeTooltip (Contextual Information Tooltip Contract)

## 1. 🎯 Fingerprint & Heuristic Matching
- **DOM Signatures:**
  - Pequeña burbuja de texto flotante de una o dos líneas, con fondo de alto contraste, flecha direccional sutil y que se activa al hacer hover o enfocar con el teclado sobre un elemento interactivo.
  - Firmas de clases utilitarias de referencia: `.tooltip`, `.tooltip-inner`, `.tooltip-arrow`, `.bs-tooltip-top|bottom|start|end`.

## 2. 📐 Component Interface & Props
```typescript
export type TooltipPlacement = 'top' | 'bottom' | 'left' | 'right';

export interface TooltipProps {
  content: string;
  children: React.ReactElement;
  placement?: TooltipPlacement;
  delay?: number; // en ms (por defecto 200ms)
}
```

## 3. ♿ Reglas de Accesibilidad (a11y) & Estados
- **Criterio WCAG 1.4.13 (Content on Hover or Focus):**
  - **Descartable:** Debe poder cerrarse con la tecla `Escape` sin mover el puntero ni el foco.
  - **Hoverable:** El puntero debe poder moverse sobre el tooltip mismo sin que este desaparezca.
  - **Persistente:** Debe permanecer visible hasta que el usuario quite el foco o mueva el ratón.
- **Asociación Semántica:**
  - El tooltip debe tener `role="tooltip"` y un `id` único.
  - El elemento disparador debe portar `aria-describedby="{tooltip-id}"` mientras el tooltip esté activo.
