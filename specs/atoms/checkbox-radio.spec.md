# SPEC: AtomCheckboxRadio (Checkbox, Radio Button & Switch Contract)

## 1. 🎯 Fingerprint & Heuristic Matching
- **DOM Signatures:**
  - Elementos `<input type="checkbox">` e `<input type="radio">`.
  - Estructuras compuestas con `<label>` adyacente o envolvente.
  - Firmas de clases utilitarias de referencia: `.form-check`, `.form-check-input`, `.form-check-label`, `.form-switch`, `.btn-check`.
  - Geometría: Contenedor cuadrado (20-24px) para checkboxes, circular para radios, y píldora con handle deslizante para switches.

## 2. 📐 Component Interface & Props
```typescript
export interface CheckboxProps extends React.InputHTMLAttributes<HTMLInputElement> {
  label?: React.ReactNode;
  isIndeterminate?: boolean;
  helperText?: string;
  errorMessage?: string;
}

export interface RadioProps extends React.InputHTMLAttributes<HTMLInputElement> {
  label?: React.ReactNode;
  helperText?: string;
}

export interface SwitchProps extends Omit<React.InputHTMLAttributes<HTMLInputElement>, 'type'> {
  label?: React.ReactNode;
  checkedLabel?: string;
  uncheckedLabel?: string;
}
```

## 3. ♿ Reglas de Accesibilidad (a11y) & Estados
- **Área Táctil (Hitbox):** El hitbox del control más su etiqueta asociada debe sumar un área interactiva mínima de **44x44px**.
- **Indeterminate State:** Cuando `isIndeterminate={true}`, el checkbox debe reflejar la propiedad JavaScript `el.indeterminate = true` y exponer `aria-checked="mixed"`.
- **Foco:** El anillo de foco debe envolver claramente el control (`outline: 3px solid #56589a; outline-offset: 2px`).
- **Estados:** Default, Checked/Selected, Focus, Disabled (`cursor: not-allowed`, opacidad reducida).
