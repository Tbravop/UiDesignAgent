# SPEC: AtomSpinner (Loading Indicator Contract)

## 1. 🎯 Fingerprint & Heuristic Matching
- **DOM Signatures:**
  - Elemento `<div>` o `<span>` con borde circular animado (`border-radius: 50%`, `animation: spin` o `rotate`), o animación pulsante (`animation: spinner-grow`).
  - Firmas de clases utilitarias de referencia: `.spinner-border`, `.spinner-grow`, `.spinner-border-sm`.
  - Típico en estados de carga de botones, páginas intermedias y fetch de datos asíncronos.

## 2. 📐 Component Interface & Props
```typescript
export type SpinnerType = 'border' | 'grow';
export type SpinnerSize = 'sm' | 'md' | 'lg';
export type SpinnerColor = 'primary' | 'secondary' | 'current' | 'light';

export interface SpinnerProps {
  type?: SpinnerType;
  size?: SpinnerSize;
  color?: SpinnerColor;
  label?: string; // Por defecto "Cargando..."
  className?: string;
}
```

## 3. ♿ Reglas de Accesibilidad (a11y) & Estados
- **Rol y Anuncios Auditivos:** Debe contener `role="status"` y una etiqueta visible solo para lectores de pantalla `<span class="sr-only">{label || "Cargando..."}</span>`.
- **Preferencia de Movimiento Reducido:** Si el usuario tiene activa la preferencia de sistema `prefers-reduced-motion: reduce`, la velocidad de animación debe desacelerarse drásticamente o sustituirse por un indicador estático o pulsación sutil.
- **Contraste:** El color del spinner debe garantizar un ratio de contraste de al menos **3:1** contra el fondo circundante.
