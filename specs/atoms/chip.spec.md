# SPEC: AtomChip (Interactive Chips & Filter Tags)

## 1. 🎯 Fingerprint & Heuristic Matching
- **DOM Signatures:**
  - Contenedores compactos con bordes redondeados o rígidos (`border-2`), padding horizontal (`0.5rem - 0.75rem`), con botón de cierre integrado (`<button aria-label="Eliminar">×</button>`) o comportamiento de selección tipo pill (`.slicer-pill`).
  - Firmas de clases utilitarias de referencia: `.btn-check + .btn-outline-*`, `.badge.interactive`, chips de búsqueda.

## 2. 📐 Component Interface & Props
```typescript
export type ChipVariant = 'default' | 'primary' | 'secondary' | 'outline';

export interface ChipProps {
  label: string;
  variant?: ChipVariant;
  isSelected?: boolean;
  isRemovable?: boolean;
  avatar?: React.ReactNode;
  icon?: React.ReactNode;
  onSelect?: () => void;
  onRemove?: () => void;
  disabled?: boolean;
}
```

## 3. ♿ Reglas de Accesibilidad (a11y) & Estados
- **Roles ARIA:**
  - Si es filtrable/seleccionable: `role="checkbox"` o `role="button"` con `aria-pressed="true|false"`.
  - Si es removible: El botón de cierre debe contener `aria-label={`Eliminar filtro ${label}`}` y recibir foco por teclado.
- **Hitbox:** Altura mínima de 36px en escritorio y hitbox ampliado a 44px en dispositivos móviles.
- **Navegación por Teclado:** Soporte para `Enter` y `Space` para seleccionar, y `Delete` o `Backspace` para remover.
