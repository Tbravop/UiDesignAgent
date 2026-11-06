# Spec: Organism — Command Palette (`organism-command-palette`)

Centro omnibox modal de búsqueda rápida y ejecución de acciones o navegación global, invocado mediante atajo de teclado (`Ctrl+K` / `Cmd+K`) o botón disparador.

---

## 1. 🎯 Fingerprint & Heuristic Matching

- **Selectores Semánticos / Estructurales:** Contenedor `<dialog>` o `<div role="dialog" aria-modal="true">` que integra en su cabecera un campo de búsqueda con `role="combobox"` (`aria-expanded="true"`, `aria-controls`) y debajo una lista filtrable con `role="listbox"` dividida en grupos (`role="group"`).
- **Heurística de Caja (Playwright):**
  - Posicionado en el tercio superior central del viewport (`max-width: 640px`, `width: 90vw`), sobre un backdrop semitransparente.
  - Combina el átomo `atom-form-input` en la parte superior, divisores `atom-separator` y una lista desplazable (`max-height: 360px; overflow-y: auto`) de opciones con iconos y badges de atajos `<kbd>`.

---

## 2. 📐 Component Interface & Props

```typescript
export interface CommandItem {
  id: string;
  label: string;
  group: string;
  keywords?: string[];
  shortcut?: string;
  href?: string;
  onExecute?: () => void;
}

export interface CommandPaletteProps {
  /** Estado de visibilidad del diálogo */
  isOpen: boolean;
  /** Texto placeholder del buscador omnibox */
  placeholder?: string;
  /** Colección de comandos y rutas disponibles */
  commands: CommandItem[];
  /** Mensaje mostrado cuando el filtro no arroja coincidencias */
  emptyMessage?: string;
  /** Callback de cierre */
  onClose: () => void;
}
```

### Mapeo a Tokens de `./DESIGN.md`
- **Marco del Diálogo:** Superficie `--color-surface-card`, borde `3px solid var(--color-on-surface)` y sombra dura máxima `--shadow-hard-lg` (`8px 8px 0px var(--color-on-surface)`).
- **Opción Seleccionada (`aria-selected="true"`):** Fondo `--color-primary` con texto blanco o `--color-accent-yellow` con texto `--color-on-surface`.

---

## 3. ♿ Reglas de Accesibilidad (a11y) & Estados

- **Gestión de Foco y Teclado:**
  - Al abrirse, el foco se coloca automáticamente en el `<input role="combobox">`.
  - `ArrowDown` / `ArrowUp` actualiza `aria-activedescendant` sobre el ítem activo (`role="option"`) sin perder el foco de escritura en el input.
  - `Escape` cierra el diálogo y restaura el foco al elemento disparador previo.
- **Estados Obligatorios:**
  - **Vacío (`Empty State`):** Si la consulta no coincide con ningún comando, anunciar el mensaje mediante `role="status"` (`aria-live="polite"`).
