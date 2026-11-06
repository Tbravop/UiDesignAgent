# SPEC: MoleculeListGroup (List Group & Action List Contract)

## 1. 🎯 Fingerprint & Heuristic Matching
- **DOM Signatures:**
  - Lista vertical u horizontal de elementos (`<ul>`, `<ol>` o `<div>`) con bordes compartidos, divisores horizontales uniformes, y soporte para ítems interactivos (`<a>`, `<button>`) con badges de conteo alineados a la derecha.
  - Firmas de clases utilitarias de referencia: `.list-group`, `.list-group-item`, `.list-group-item-action`, `.list-group-flush`, `.list-group-horizontal`.

## 2. 📐 Component Interface & Props
```typescript
export interface ListGroupItem {
  id: string;
  content: React.ReactNode;
  badge?: React.ReactNode;
  isActive?: boolean;
  isDisabled?: boolean;
  href?: string;
  onClick?: () => void;
}

export interface ListGroupProps {
  items: ListGroupItem[];
  isFlush?: boolean;
  isHorizontal?: boolean;
  isNumbered?: boolean;
  ariaLabel?: string;
}
```

## 3. ♿ Reglas de Accesibilidad (a11y) & Estados
- **Semántica:** Si los ítems no son interactivos, estructurar con `<ul>` / `<li>`. Si son seleccionables, utilizar `role="listbox"` y `role="option"` con `aria-selected="true|false"`.
- **Estados:**
  - `Active`: Indicador visual contrastante y atributo semántico (`aria-current="true"` si es enlace, o `aria-selected="true"` si es opción).
  - `Disabled`: `aria-disabled="true"`, sin eventos de interacción.
- **Hitbox:** Cada ítem interactivo debe garantizar al menos **44px** de altura mínima para toques táctiles.
