# SPEC: MoleculeAlert (Contextual Alert Notification Contract)

## 1. 🎯 Fingerprint & Heuristic Matching
- **DOM Signatures:**
  - Contenedor en bloque con borde perimetral, fondo temático (success, warning, error, info), icono decorativo/semántico opcional y un botón de cierre opcional (`.btn-close` o `atom-close-button`).
  - Firmas de clases utilitarias de referencia: `.alert`, `.alert-primary`, `.alert-success`, `.alert-danger`, `.alert-dismissible`.
  - Usado para feedback inmediato al usuario tras acciones o estados del sistema.

## 2. 📐 Component Interface & Props
```typescript
export type AlertVariant = 'primary' | 'secondary' | 'success' | 'warning' | 'danger' | 'info';

export interface AlertProps {
  variant?: AlertVariant;
  title?: string;
  children: React.ReactNode;
  icon?: React.ReactNode;
  isDismissible?: boolean;
  onDismiss?: () => void;
  action?: React.ReactNode;
}
```

## 3. ♿ Reglas de Accesibilidad (a11y) & Estados
- **Rol y Anuncios Dinámicos:**
  - Si aparece dinámicamente como mensaje de error urgente: `role="alert"` (implica `aria-live="assertive"`).
  - Si es una notificación informativa o de estado: `role="status"` (`aria-live="polite"`).
- **Contraste:** Tanto el texto interior como los iconos deben cumplir con un ratio mínimo de **4.5:1** contra el fondo de la alerta (`oklch`).
- **Botón de Cierre:** Debe ser operable por teclado (`Tab`, `Enter`, `Space`) y contener `aria-label="Cerrar alerta"`.
