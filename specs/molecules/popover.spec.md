# SPEC: MoleculePopover (Contextual Popover Overlay Contract)

## 1. 🎯 Fingerprint & Heuristic Matching
- **DOM Signatures:**
  - Contenedor flotante vinculado a un elemento disparador, con cabecera de título (`.popover-header`), cuerpo de contenido enriquecido (`.popover-body`) y una flecha/puntero direccional triangular (`.popover-arrow`).
  - Firmas de clases utilitarias de referencia: `.popover`, `.popover-header`, `.popover-body`, `.bs-popover-top|bottom|start|end`.

## 2. 📐 Component Interface & Props
```typescript
export type PopoverPlacement = 'top' | 'bottom' | 'left' | 'right';

export interface PopoverProps {
  trigger: React.ReactNode;
  title?: React.ReactNode;
  content: React.ReactNode;
  placement?: PopoverPlacement;
  isOpen?: boolean;
  onToggle?: (open: boolean) => void;
  hasArrow?: boolean;
}
```

## 3. ♿ Reglas de Accesibilidad (a11y) & Estados
- **Semántica:** El contenedor del popover debe tener `role="dialog"` con `aria-labelledby="{title-id}"`.
- **Disparador:** El botón disparador debe portar `aria-haspopup="dialog"`, `aria-expanded="true|false"` y `aria-controls="{popover-id}"`.
- **Cierre por Teclado:** Presionar `Escape` debe cerrar el popover y restaurar el foco al disparador.
- **Trampa de Foco Opcional:** Si el popover contiene elementos interactivos (botones, formularios), debe permitir tabulación interna cíclica o cierre accesible.
