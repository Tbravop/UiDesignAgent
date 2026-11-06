# SPEC: OrganismModal (Modal Dialog Overlay Contract)

## 1. 🎯 Fingerprint & Heuristic Matching
- **DOM Signatures:**
  - Capa superpuesta fija (`.modal-backdrop`) que bloquea la interacción con la página principal, centrando una ventana emergente (`.modal-dialog`) compuesta por cabecera (`.modal-header`), botón de cierre (`atom-close-button`), cuerpo escroleable (`.modal-body`) y pie con botones de acción (`.modal-footer`).
  - Firmas de clases utilitarias de referencia: `.modal`, `.modal-dialog`, `.modal-content`, `.modal-header`, `.modal-body`, `.modal-footer`, `.modal-dialog-centered`, `.modal-dialog-scrollable`.

## 2. 📐 Component Interface & Props
```typescript
export type ModalSize = 'sm' | 'md' | 'lg' | 'xl' | 'fullscreen';

export interface ModalProps {
  isOpen: boolean;
  onClose: () => void;
  title: React.ReactNode;
  children: React.ReactNode;
  footer?: React.ReactNode;
  size?: ModalSize;
  isCentered?: boolean;
  isScrollable?: boolean;
  closeOnBackdropClick?: boolean;
  closeOnEsc?: boolean;
}
```

## 3. ♿ Reglas de Accesibilidad (a11y) & Estados
- **Patrón WAI-ARIA Modal Dialog:**
  - El contenedor principal debe tener `role="dialog"`, `aria-modal="true"` y estar rotulado mediante `aria-labelledby="{title-id}"`.
  - Si no tiene título visual, debe llevar `aria-label="Nombre del diálogo"`.
- **Trampa de Foco (Focus Trap):**
  - Al abrirse, el foco debe moverse al primer elemento interactivo del diálogo o al botón de cierre.
  - El usuario no debe poder tabular fuera del diálogo mientras esté abierto (`inert` en el resto del DOM).
  - Al cerrarse, el foco debe retornar exactamente al elemento que lo abrió.
- **Cierre por Teclado:** Presionar `Escape` debe invocar `onClose()`.
