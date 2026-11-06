# SPEC: OrganismOffcanvas (Offcanvas Drawer & Sidebar Panel Contract)

## 1. 🎯 Fingerprint & Heuristic Matching
- **DOM Signatures:**
  - Panel lateral deslizante oculto fuera del viewport (`.offcanvas`), que se desliza suavemente hacia el interior desde el lateral izquierdo, derecho, superior o inferior (`.offcanvas-start|end|top|bottom`) al activarse mediante un disparador, oscureciendo el fondo con backdrop opcional.
  - Firmas de clases utilitarias de referencia: `.offcanvas`, `.offcanvas-header`, `.offcanvas-title`, `.offcanvas-body`, `.offcanvas-start`, `.offcanvas-end`.
  - Típico en menús móviles, filtros laterales de catálogos y paneles de configuración.

## 2. 📐 Component Interface & Props
```typescript
export type OffcanvasPlacement = 'start' | 'end' | 'top' | 'bottom';

export interface OffcanvasProps {
  isOpen: boolean;
  onClose: () => void;
  title: React.ReactNode;
  children: React.ReactNode;
  placement?: OffcanvasPlacement;
  hasBackdrop?: boolean;
  allowBodyScroll?: boolean;
}
```

## 3. ♿ Reglas de Accesibilidad (a11y) & Estados
- **Patrón WAI-ARIA Dialog:**
  - Debe portar `role="dialog"`, `aria-modal="true"` y estar rotulado mediante `aria-labelledby="{title-id}"`.
- **Trampa de Foco (Focus Trap):**
  - Al abrirse, trasladar el foco al botón de cierre o al primer elemento interactivo del panel.
  - Bloquear la tabulación al contenido principal oculto bajo el backdrop (`inert`).
  - Al cerrarse, devolver el foco al disparador original.
- **Cierre por Teclado:** Presionar `Escape` debe cerrar el panel lateral.
- **Botón de Cierre:** El `atom-close-button` de la cabecera debe tener `aria-label="Cerrar menú lateral"`.
