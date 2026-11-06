# SPEC: MoleculeButtonGroup (Segmented Control & Button Group Contract)

## 1. 🎯 Fingerprint & Heuristic Matching
- **DOM Signatures:**
  - Contenedor en bloque (`display: inline-flex` o `flex`) que agrupa dos o más botones adyacentes (`atom-button`), colapsando sus bordes intermedios para formar una barra única.
  - Firmas de clases utilitarias de referencia: `.btn-group`, `.btn-group-vertical`, `.btn-group-sm|lg`.
  - Usado para controles segmentados (ej. Vista Lista / Vista Cuadrícula), barras de herramientas o botones divididos (`split-button`).

## 2. 📐 Component Interface & Props
```typescript
export type ButtonGroupOrientation = 'horizontal' | 'vertical';
export type ButtonGroupSize = 'sm' | 'md' | 'lg';

export interface ButtonGroupProps {
  children: React.ReactNode;
  orientation?: ButtonGroupOrientation;
  size?: ButtonGroupSize;
  ariaLabel: string; // Obligatorio para agrupar semánticamente
  isAttached?: boolean;
}
```

## 3. ♿ Reglas de Accesibilidad (a11y) & Estados
- **Rol de Grupo:** El contenedor debe portar `role="group"` y una etiqueta descriptiva mediante `aria-label` (ej. `aria-label="Controles de formato de texto"`).
- **Controles Segmentados:** Si funciona como selector de opción única, debe usar `role="radiogroup"` y sus botones deben incluir `role="radio"` con `aria-checked="true|false"`.
- **Navegación por Teclado:** Flechas direccionales (`ArrowLeft` / `ArrowRight` o `ArrowUp` / `ArrowDown`) para alternar entre opciones en grupos de selección.
- **Manejo de Foco:** El botón enfocado debe elevar su `z-index` para mostrar su outline completo sin recortes.
