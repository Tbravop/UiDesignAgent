# SPEC: AtomFormInput (Text Input & Textarea Contract)

## 1. 🎯 Fingerprint & Heuristic Matching
- **DOM Signatures:**
  - Elementos `<input type="text|email|password|number|tel|url|search">` y `<textarea>`.
  - Firmas de clases utilitarias de referencia: `.form-control`, `.form-control-plaintext`, `.form-control-lg`, `.form-control-sm`.
  - Propiedades computadas: Fondo claro (`#ffffff` / canvas), borde perimetral (mínimo 2px), padding interno (`0.5rem 0.75rem`), fuente mono o sans-serif legible.

## 2. 📐 Component Interface & Props
```typescript
export type InputSize = 'sm' | 'md' | 'lg';
export type InputStatus = 'default' | 'success' | 'warning' | 'error';

export interface FormInputProps extends Omit<React.InputHTMLAttributes<HTMLInputElement>, 'size'> {
  label?: string;
  helperText?: string;
  errorMessage?: string;
  size?: InputSize;
  status?: InputStatus;
  isClearable?: boolean;
  prefixNode?: React.ReactNode;
  suffixNode?: React.ReactNode;
}

export interface FormTextareaProps extends React.TextareaHTMLAttributes<HTMLTextAreaElement> {
  label?: string;
  helperText?: string;
  errorMessage?: string;
  status?: InputStatus;
  autoResize?: boolean;
}
```

## 3. ♿ Reglas de Accesibilidad (a11y) & Estados
- **Asociación de Etiquetas:** Todo input debe estar vinculado a un `<label>` explícito mediante `id` y `for`/`htmlFor`.
- **Mensajería Accesible:** Si `errorMessage` está presente:
  - Input debe tener `aria-invalid="true"`.
  - El mensaje de error debe vincularse al input mediante `aria-describedby="{id}-error"`.
  - El contenedor de error debe tener `role="alert"`.
- **Estados Visuales:**
  - `Default`: Borde estándar (`2px solid #1c1b1b`).
  - `Focus`: Borde o anillo de foco contrastante (3px solid `#56589a` o hard-shadow) sin pérdida del cursor.
  - `Error`: Borde destructivo (`#ef4444` / `#ba1a1a`) y texto de validación.
  - `Disabled`: `aria-disabled="true"`, fondo atenuado (`#eae7e7`), cursor `not-allowed`.
