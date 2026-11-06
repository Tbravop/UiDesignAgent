# SPEC: MoleculeInputGroup (Input Groups with Addons & Buttons)

## 1. 🎯 Fingerprint & Heuristic Matching
- **DOM Signatures:**
  - Contenedor flexible (`display: flex`) que une directamente un `<input>` con uno o más elementos periféricos (etiquetas prefijo/sufijo tipo `$`, `@`, `.com`, o botones de acción como "Buscar", "Copiar").
  - Firmas de clases utilitarias de referencia: `.input-group`, `.input-group-text`, `.input-group-prepend`, `.input-group-append`.
  - Geometría de bordes compartidos: los elementos internos colapsan sus bordes intermedios (`margin-left: -1px` o `border-radius: 0`) para formar una sola unidad visual sólida.

## 2. 📐 Component Interface & Props
```typescript
export interface InputGroupProps {
  id?: string;
  label?: string;
  prependAddon?: React.ReactNode;
  appendAddon?: React.ReactNode;
  prependButton?: React.ReactNode;
  appendButton?: React.ReactNode;
  inputProps: React.InputHTMLAttributes<HTMLInputElement>;
  helperText?: string;
  errorMessage?: string;
}
```

## 3. ♿ Reglas de Accesibilidad (a11y) & Estados
- **Agrupamiento Semántico:** Si el grupo contiene múltiples controles interactivos (ej. input + botón de acción), el contenedor debe organizarse con un `<label>` claro para el input y nombres accesibles independientes para cada botón (`aria-label`).
- **Preservación del Focus Ring:** Al recibir foco, el input o botón activo debe elevar su `z-index` (ej. `z-index: 2`) para que su borde o sombra de foco no quede tapado por los bordes adyacentes.
- **Validación Visual:** El estado de error (`aria-invalid="true"`) debe teñir el borde perimetral del grupo completo o reflejarse con icono y mensaje descriptivo.
