# SPEC: MoleculeToast (Toast Notification Message Contract)

## 1. 🎯 Fingerprint & Heuristic Matching
- **DOM Signatures:**
  - Contenedor rectangular flotante o apilable en esquinas de pantalla (`.toast-container`), con cabecera (`.toast-header`) que incluye icono, título, marca de tiempo y botón de cierre (`atom-close-button`), y un cuerpo descriptivo (`.toast-body`).
  - Firmas de clases utilitarias de referencia: `.toast`, `.toast-container`, `.toast-header`, `.toast-body`.

## 2. 📐 Component Interface & Props
```typescript
export type ToastVariant = 'default' | 'success' | 'warning' | 'error' | 'info';

export interface ToastProps {
  id: string;
  title: string;
  message: React.ReactNode;
  timestamp?: string;
  variant?: ToastVariant;
  duration?: number; // en ms (por defecto 5000ms, o 0 para persistente)
  isDismissible?: boolean;
  onDismiss?: (id: string) => void;
}
```

## 3. ♿ Reglas de Accesibilidad (a11y) & Estados
- **Semántica Live Region:**
  - Si es una notificación crítica/error: `role="alert"` y `aria-live="assertive"`.
  - Si es informativa o de confirmación: `role="status"` y `aria-live="polite"`.
  - El contenedor debe incluir `aria-atomic="true"`.
- **Tiempo Suficiente:** Si el toast desaparece automáticamente, debe permitir pausar el temporizador mientras el puntero esté encima (`onMouseEnter`) o mientras mantenga el foco por teclado.
- **Botón de Cierre:** Debe incluir `aria-label="Cerrar notificación"`.
