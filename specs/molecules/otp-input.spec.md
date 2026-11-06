# SPEC: MoleculeOtpInput (Segmented One-Time Password Input)

## 1. 🎯 Fingerprint & Heuristic Matching
- **DOM Signatures:**
  - Grupo de 4 a 8 campos de entrada individuales (`<input type="text|tel|password">` o `maxlength="1"`), dispuestos horizontalmente con `display: flex`, espacio uniforme (`gap-2` a `gap-4`) y dimensiones cuadradas (ej. 44x44px a 56x56px).
  - Típico en flujos de autenticación 2FA, verificación SMS y códigos de seguridad bancarios.
  - Comportamiento de auto-foco progresivo hacia la derecha al ingresar un dígito y retroceso al presionar `Backspace`.

## 2. 📐 Component Interface & Props
```typescript
export interface OtpInputProps {
  length?: number; // Por defecto 6
  value: string;
  onChange: (value: string) => void;
  onComplete?: (code: string) => void;
  isMasked?: boolean;
  isNumericOnly?: boolean;
  isDisabled?: boolean;
  hasError?: boolean;
  errorMessage?: string;
  autoFocusFirst?: boolean;
}
```

## 3. ♿ Reglas de Accesibilidad (a11y) & Estados
- **Estructura Accesible:**
  - El grupo de inputs debe envolverse en un `<fieldset>` con un `<legend class="sr-only">Código de verificación de {length} dígitos</legend>`.
  - Cada input individual debe contar con `aria-label={`Dígito ${index + 1} de ${length}`}`.
- **Soporte Pegado (Clipboard Paste):** Al pegar un código completo desde el portapapeles (`onPaste`), el componente debe distribuir automáticamente los caracteres a lo largo de las casillas correspondientes y disparar `onComplete`.
- **Modo Input Móvil:** `inputMode="numeric"` y `pattern="[0-9]*"` para abrir el teclado numérico en smartphones.
- **Focus Ring:** Cada casilla activa debe resaltar con borde contrastante (ej. 3px sólido o sombra dura neo-brutalista).
