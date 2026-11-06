# Spec: Molecule — Context Menu (`molecule-context-menu`)

Menú emergente de acciones contextuales que se despliega en las coordenadas del cursor al invocar el evento de clic secundario (`contextmenu`) o mediante la tecla de menú contextual del teclado.

---

## 1. 🎯 Fingerprint & Heuristic Matching

- **Selectores Semánticos / Estructurales:** Contenedor con `role="menu"` posicionado en coordenadas `(clientX, clientY)` que agrupa elementos con `role="menuitem"`, `role="menuitemcheckbox"`, `role="menuitemradio"` y divisores `role="separator"`.
- **Heurística de Caja (Playwright):**
  - Lista vertical compacta (`min-width: 180px`, `max-width: 280px`), borde de `3px` y sombra dura.
  - Cada opción interactiva presenta alineación horizontal (`display: flex; justify-content: space-between`) para mostrar la etiqueta a la izquierda y el atajo de teclado (`<kbd>`) a la derecha.

---

## 2. 📐 Component Interface & Props

```typescript
export interface ContextMenuItem {
  id: string;
  label: string;
  shortcut?: string;
  disabled?: boolean;
  danger?: boolean;
  onSelect?: () => void;
}

export interface ContextMenuProps {
  /** Lista de elementos o grupos separados del menú contextual */
  items: Array<ContextMenuItem | 'separator'>;
  /** Etiqueta accesible para el contenedor role="menu" */
  ariaLabel: string;
}
```

### Mapeo a Tokens de `./DESIGN.md`
- **Contenedor:** Fondo `--color-surface-card`, borde `3px solid var(--color-on-surface)`, sombra `--shadow-hard-md`.
- **Estado Activo / Foco de Ítem:** Fondo `--color-accent-yellow` (`oklch(0.91 0.13 92)`) o `--color-primary` para acciones destructivas (`danger`), garantizando contraste WCAG AA.

---

## 3. ♿ Reglas de Accesibilidad (a11y) & Estados

- **Navegación WAI-ARIA Menu:**
  - `ArrowDown` / `ArrowUp`: recorre circularmente los elementos `role="menuitem"` habilitados.
  - `Enter` / `Space`: ejecuta la acción del ítem enfocado y cierra el menú.
  - `Escape`: cierra el menú y devuelve el foco al elemento que recibió la invocación original.
- **Hitbox:** Cada ítem debe mantener una altura mínima cómoda (`>= 36px` en escritorio, `>= 44px` en dispositivos táctiles).
