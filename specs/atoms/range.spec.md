# SPEC: AtomRange (Range Slider Control Contract)

## 1. 🎯 Fingerprint & Heuristic Matching
- **DOM Signatures:**
  - Elemento nativo `<input type="range">`.
  - Firmas de clases utilitarias de referencia: `.form-range`.
  - Compuesto por una pista horizontal (`track`) y un deslizador manipulable (`thumb`).
  - Utilizado para selecciones continuas o discretas (volumen, precios, porcentajes).

## 2. 📐 Component Interface & Props
```typescript
export interface RangeProps extends Omit<React.InputHTMLAttributes<HTMLInputElement>, 'type'> {
  min?: number;
  max?: number;
  step?: number;
  value?: number;
  label?: string;
  showValueBadge?: boolean;
  formatValue?: (val: number) => string;
  helperText?: string;
}
```

## 3. ♿ Reglas de Accesibilidad (a11y) & Estados
- **Semántica ARIA:** Si no existe un `<label>` visible adyacente, debe incluir `aria-label` o `aria-labelledby`.
- **Valores Actuales:** `aria-valuemin`, `aria-valuemax`, `aria-valuenow` y opcionalmente `aria-valuetext` para formatos humanizados (ej. "$50.000 CLP").
- **Navegación por Teclado:**
  - `ArrowRight` / `ArrowUp`: Incrementar un `step`.
  - `ArrowLeft` / `ArrowDown`: Decrementar un `step`.
  - `PageUp` / `PageDown`: Salto mayor (ej. 10% del rango).
  - `Home` / `End`: Ir a valor mínimo / máximo.
- **Hitbox:** El `thumb` interactivo debe proporcionar un área táctil mínima de **44x44px** mediante padding invisible.
