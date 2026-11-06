# SPEC: AtomProgress (Progress Bar Indicator Contract)

## 1. 🎯 Fingerprint & Heuristic Matching
- **DOM Signatures:**
  - Contenedor de barra externa con altura fija (ej. 4px a 24px) y un elemento interno con anchura porcentual variable (`style="width: X%"`).
  - Firmas de clases utilitarias de referencia: `.progress`, `.progress-bar`, `.progress-bar-striped`, `.progress-bar-animated`.
  - Típico en subida de archivos, pasos de onboarding, indicadores de nivel y batería.

## 2. 📐 Component Interface & Props
```typescript
export type ProgressVariant = 'primary' | 'secondary' | 'success' | 'warning' | 'danger';

export interface ProgressProps {
  value: number; // 0 a 100
  max?: number;  // Por defecto 100
  variant?: ProgressVariant;
  height?: number | string;
  showLabel?: boolean;
  isStriped?: boolean;
  isAnimated?: boolean;
  ariaLabel?: string;
}
```

## 3. ♿ Reglas de Accesibilidad (a11y) & Estados
- **Semántica WAI-ARIA:**
  - El elemento de progreso debe portar `role="progressbar"`.
  - Atributos obligatorios: `aria-valuenow={value}`, `aria-valuemin={0}`, `aria-valuemax={max || 100}`.
  - Si no hay texto visible que describa la tarea, debe incluir `aria-label` (ej. `aria-label="Progreso de subida del archivo"`).
- **Contraste:** El relleno de la barra contra el fondo del track debe cumplir con un ratio de contraste de al menos **3:1** (`oklch`).
- **Movimiento Reducido:** Las barras con animación de rayas (`.progress-bar-animated`) deben detener su animación continua bajo `prefers-reduced-motion: reduce`.
