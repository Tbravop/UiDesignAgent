# SPEC: MoleculeFloatingLabel (Floating Label Form Input Contract)

## 1. 🎯 Fingerprint & Heuristic Matching
- **DOM Signatures:**
  - Contenedor relativo que combina un `<input>` o `<select>` con un `<label>` superpuesto dentro del área del campo, el cual reduce su escala y se desplaza hacia la parte superior al recibir foco o cuando el campo contiene valor.
  - Firmas de clases utilitarias de referencia: `.form-floating`.
  - Propiedad clave: el `<input>` debe anteceder al `<label>` para permitir el selector CSS hermano `input:focus ~ label, input:not(:placeholder-shown) ~ label`.

## 2. 📐 Component Interface & Props
```typescript
export interface FloatingLabelProps extends React.InputHTMLAttributes<HTMLInputElement> {
  label: string;
  id: string; // Obligatorio para vincular input y label
  helperText?: string;
  errorMessage?: string;
  hasError?: boolean;
}
```

## 3. ♿ Reglas de Accesibilidad (a11y) & Estados
- **Placeholder Invisible Oculto:** El input debe contener un placeholder no vacío (ej. `placeholder=" "`) para que el navegador soporte el pseudo-selector `:not(:placeholder-shown)` sin interferir con la etiqueta visual.
- **Vínculo Estricto:** El `<label>` debe tener el atributo `for="{id}"` exactamente igual al `id` del input.
- **Legibilidad de Foco:** Cuando la etiqueta flota en la parte superior, su tamaño de fuente reducido (ej. 11px o 12px) debe mantener un ratio de contraste de al menos **4.5:1** contra el fondo del input.
- **Mensaje de Error:** Al fallar la validación, vincular con `aria-describedby="{id}-error"` y `aria-invalid="true"`.
