# SPEC: OrganismAccordion (Accordion & Collapsible Panels Contract)

## 1. 🎯 Fingerprint & Heuristic Matching
- **DOM Signatures:**
  - Grupo vertical de paneles apilados (`.accordion-item`), donde cada panel consta de un encabezado (`.accordion-header`) con un botón disparador (`.accordion-button`) y un contenedor colapsable (`.accordion-collapse`) con el cuerpo del contenido (`.accordion-body`).
  - Firmas de clases utilitarias de referencia: `.accordion`, `.accordion-item`, `.accordion-header`, `.accordion-button`, `.accordion-collapse`, `.accordion-body`, `.accordion-flush`.

## 2. 📐 Component Interface & Props
```typescript
export interface AccordionItem {
  id: string;
  title: React.ReactNode;
  content: React.ReactNode;
  isDisabled?: boolean;
}

export interface AccordionProps {
  items: AccordionItem[];
  allowMultiple?: boolean; // Permite abrir varios paneles a la vez
  defaultExpandedIds?: string[];
  isFlush?: boolean;
}
```

## 3. ♿ Reglas de Accesibilidad (a11y) & Estados
- **Patrón WAI-ARIA Accordion:**
  - Cada botón dentro del encabezado (`h2-h6`) debe tener `aria-expanded="true|false"` y `aria-controls="{collapse-id}"`.
  - El contenedor colapsable debe tener `id="{collapse-id}"` y `role="region"` con `aria-labelledby="{button-id}"`.
- **Navegación por Teclado:**
  - `Tab`: Navega entre los botones de encabezado de los acordeones.
  - `Enter` o `Space`: Alterna la expansión/colapso del panel enfocado.
  - Opcional: `ArrowDown` / `ArrowUp` para mover el foco entre los encabezados del acordeón.
- **Hitbox:** Cada botón de acordeón debe tener una altura mínima de contacto de **44px**.
