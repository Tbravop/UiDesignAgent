# SPEC: MoleculePasswordStrength (Password Input with Real-Time Strength Meter)

## 1. 🎯 Fingerprint & Heuristic Matching
- **DOM Signatures:**
  - Campo de entrada de contraseña (`<input type="password">`) con botón toggle para alternar visibilidad (icono de ojo / visibilidad), acompañado inmediatamente por una barra de progreso segmentada o continua y una lista de requisitos (mayúsculas, números, longitud, símbolos).
  - Típico en formularios de registro, onboarding y reseteo de credenciales.
  - Comportamiento de actualización dinámica de la barra de fortaleza (débil, media, fuerte, muy fuerte) a medida que el usuario escribe.

## 2. 📐 Component Interface & Props
```typescript
export type PasswordStrengthLevel = 'empty' | 'weak' | 'fair' | 'good' | 'strong';

export interface PasswordRule {
  id: string;
  label: string;
  validator: (password: string) => boolean;
}

export interface PasswordStrengthProps {
  value: string;
  onChange: (value: string) => void;
  rules?: PasswordRule[];
  showVisibilityToggle?: boolean;
  label?: string;
  helperText?: string;
  onStrengthChange?: (level: PasswordStrengthLevel, score: number) => void;
}
```

## 3. ♿ Reglas de Accesibilidad (a11y) & Estados
- **Toggle de Visibilidad:** El botón de alternancia mostrar/ocultar contraseña debe tener `aria-label="Mostrar contraseña"` o `"Ocultar contraseña"` y `aria-pressed="true|false"`.
- **Anuncios en Vivo (Live Regions):**
  - El indicador de fortaleza debe contar con `role="status"` o `aria-live="polite"` para anunciar cambios de nivel (ej. "Nivel de seguridad: Fuerte") a usuarios de lectores de pantalla sin interrumpir la escritura.
- **Lista de Criterios:** Los ítems cumplidos deben reflejar `aria-checked="true"` o un prefijo audible (ej. `<span class="sr-only">Cumplido:</span>`) además de los colores visuales (`oklch`).
- **Contraste de Barra:** Las barras de colores (rojo, amarillo, verde) deben complementarse con texto descriptivo para usuarios con daltonismo.
