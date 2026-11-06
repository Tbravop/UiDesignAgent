# SPEC: MoleculeDropdown (Dropdown Menu & Split Button Contract)

## 1. 🎯 Fingerprint & Heuristic Matching
- **DOM Signatures:**
  - Botón disparador con indicador visual de chevron (`.dropdown-toggle`), que al activarse despliega un menú flotante con lista de acciones o enlaces (`.dropdown-menu`).
  - Firmas de clases utilitarias de referencia: `.dropdown`, `.dropup`, `.dropstart`, `.dropend`, `.dropdown-toggle`, `.dropdown-menu`, `.dropdown-item`, `.dropdown-divider`.

## 2. 📐 Component Interface & Props
```typescript
export interface DropdownItem {
  id: string;
  label: string;
  icon?: React.ReactNode;
  href?: string;
  onClick?: () => void;
  isDivider?: boolean;
  isDisabled?: boolean;
}

export interface DropdownProps {
  trigger: React.ReactNode;
  items: DropdownItem[];
  placement?: 'bottom-start' | 'bottom-end' | 'top-start' | 'top-end';
  isOpen?: boolean;
  onToggle?: (open: boolean) => void;
}
```

## 3. ♿ Reglas de Accesibilidad (a11y) & Estados
- **Patrón WAI-ARIA Menu Button:**
  - El botón disparador debe portar `aria-haspopup="menu"`, `aria-expanded="true|false"` y `aria-controls="{menu-id}"`.
  - El menú flotante debe tener `role="menu"` y sus elementos `role="menuitem"`.
- **Navegación por Teclado:**
  - `Enter` / `Space` / `ArrowDown`: Abre el menú y enfoca el primer ítem.
  - `ArrowDown` / `ArrowUp`: Navega secuencialmente entre ítems (saltando divisores o ítems deshabilitados).
  - `Escape`: Cierra el menú y devuelve el foco al botón disparador.
- **Hitbox:** Cada ítem del menú debe contar con un área táctil mínima de **40px a 44px**.
