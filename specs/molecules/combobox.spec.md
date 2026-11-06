# SPEC: MoleculeCombobox (Searchable Select & Autocomplete Dropdown)

## 1. 🎯 Fingerprint & Heuristic Matching
- **DOM Signatures:**
  - Control compuesto por un campo de texto interactivo (`role="combobox"`), un botón de apertura/expansión de menú con chevron/flecha, y una lista desplegable flotante (`role="listbox"`) que contiene opciones seleccionables (`role="option"`).
  - Firmas de clases utilitarias de referencia: `.form-select`, dropdown select filters, search-select widgets.
  - Comportamiento de filtrado en tiempo real según el texto tipeado.

## 2. 📐 Component Interface & Props
```typescript
export interface ComboboxOption<T = string> {
  value: T;
  label: string;
  description?: string;
  icon?: React.ReactNode;
  disabled?: boolean;
}

export interface ComboboxProps<T = string> {
  options: ComboboxOption<T>[];
  value?: T | T[];
  isMultiSelect?: boolean;
  isSearchable?: boolean;
  placeholder?: string;
  label?: string;
  helperText?: string;
  errorMessage?: string;
  onChange: (value: T | T[]) => void;
  onSearchChange?: (query: string) => void;
  isLoading?: boolean;
  disabled?: boolean;
}
```

## 3. ♿ Reglas de Accesibilidad (a11y) & Estados
- **Patrón WAI-ARIA 1.2 Combobox:**
  - El input principal debe portar `role="combobox"`, `aria-autocomplete="list"`, `aria-expanded="true|false"` y `aria-controls="{listbox-id}"`.
  - La opción activa resaltada con el teclado debe vincularse mediante `aria-activedescendant="{option-id}"`.
  - Las opciones dentro de `role="listbox"` deben tener `role="option"` y `aria-selected="true|false"`.
- **Navegación por Teclado:**
  - Flechas `ArrowDown` / `ArrowUp` para navegar por la lista.
  - `Enter` para confirmar la opción resaltada.
  - `Escape` para cerrar el dropdown y devolver el foco al input.
- **Hitbox:** Cada opción en el listbox desplegable debe contar con una altura mínima de 40px (44px recomendado en touch).
