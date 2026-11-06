# SPEC: OrganismNavsTabs (Tabbed Interface & Navigation Panels Contract)

## 1. 🎯 Fingerprint & Heuristic Matching
- **DOM Signatures:**
  - Tira horizontal de pestañas interactivas (`.nav-tabs`, `.nav-pills`) vinculadas unívocamente a paneles de contenido asociados (`.tab-content`, `.tab-pane`), donde solo un panel está visible a la vez (`.active.show`).
  - Firmas de clases utilitarias de referencia: `.nav`, `.nav-tabs`, `.nav-pills`, `.nav-item`, `.nav-link`, `.tab-content`, `.tab-pane`.

## 2. 📐 Component Interface & Props
```typescript
export interface TabItem {
  id: string;
  title: React.ReactNode;
  content: React.ReactNode;
  icon?: React.ReactNode;
  isDisabled?: boolean;
}

export interface NavsTabsProps {
  tabs: TabItem[];
  activeTabId?: string;
  onTabChange?: (tabId: string) => void;
  variant?: 'tabs' | 'pills' | 'underline';
  isFullWidth?: boolean;
}
```

## 3. ♿ Reglas de Accesibilidad (a11y) & Estados
- **Patrón WAI-ARIA Tabs:**
  - La lista de pestañas debe tener `role="tablist"`.
  - Cada pestaña individual debe tener `role="tab"`, `aria-selected="true|false"`, `aria-controls="{panel-id}"` e `id="{tab-id}"`.
  - Cada panel de contenido debe tener `role="tabpanel"`, `id="{panel-id}"`, `aria-labelledby="{tab-id}"` y `tabIndex={0}` si contiene contenido escroleable.
- **Navegación por Teclado:**
  - `ArrowLeft` / `ArrowRight`: Navega secuencialmente entre las pestañas activas.
  - `Home` / `End`: Salta a la primera / última pestaña.
  - `Space` o `Enter`: Activa la pestaña enfocada (si la selección no es automática con flechas).
