# SPEC: MoleculeDatepicker (Date & Time Picker with Calendar Popover)

## 1. 🎯 Fingerprint & Heuristic Matching
- **DOM Signatures:**
  - Campo de entrada con icono de calendario o formato de fecha (`DD/MM/AAAA`), que al activarse despliega un popover flotante conteniendo una grilla de días (mes en curso), selectores de mes/año y botones de navegación previa/siguiente.
  - Comportamiento de selección interactiva de fechas individuales, rangos (`startDate` a `endDate`) o selección de horas.

## 2. 📐 Component Interface & Props
```typescript
export type DatePickerMode = 'single' | 'range' | 'multiple';

export interface DatepickerProps {
  value?: Date | [Date, Date] | null;
  mode?: DatePickerMode;
  minDate?: Date;
  maxDate?: Date;
  disabledDates?: (date: Date) => boolean;
  dateFormat?: string; // ej. "YYYY-MM-DD"
  placeholder?: string;
  label?: string;
  helperText?: string;
  errorMessage?: string;
  onChange: (date: Date | [Date, Date] | null) => void;
  isClearable?: boolean;
  disabled?: boolean;
}
```

## 3. ♿ Reglas de Accesibilidad (a11y) & Estados
- **Patrón WAI-ARIA Grid para Calendario:**
  - El popover del calendario debe usar `role="dialog"` con `aria-modal="true"` o `aria-haspopup="dialog"`.
  - La tabla mensual de fechas debe tener `role="grid"` con `role="row"` y celdas `role="gridcell"`.
  - El día seleccionado debe portar `aria-selected="true"`.
  - El día de hoy debe indicarse mediante `aria-current="date"`.
- **Navegación por Teclado:**
  - `ArrowLeft` / `ArrowRight`: Día anterior / siguiente.
  - `ArrowUp` / `ArrowDown`: Misma semana anterior / siguiente.
  - `PageUp` / `PageDown`: Mes anterior / siguiente.
  - `Enter` / `Space`: Seleccionar la fecha activa.
  - `Escape`: Cerrar el calendario y devolver el foco al input.
- **Hitbox de Fechas:** Cada celda interactiva del calendario debe contar con un hitbox mínimo de **44x44px** en dispositivos táctiles.
