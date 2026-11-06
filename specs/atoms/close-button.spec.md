# SPEC: AtomCloseButton (Dismissal Action Button)

## 1. 🎯 Fingerprint & Heuristic Matching
- **DOM Signatures:**
  - Elemento `<button type="button">` sin texto visible directo, conteniendo típicamente una cruz SVG, un carácter "×" o fondo `background-image` con cruz SVG codificada.
  - Firmas de clases utilitarias de referencia: `.btn-close`, `.btn-close-white`.
  - Dimensiones compactas estándar: `1em x 1em` (hitbox con padding para alcanzar al menos 32px-44px).
  - Típico en cabeceras de `.modal-header`, alertas descartables `.alert-dismissible`, `.toast-header` y paneles `.offcanvas-header`.

## 2. 📐 Component Interface & Props
```typescript
export type CloseButtonVariant = 'default' | 'white' | 'subtle';

export interface CloseButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: CloseButtonVariant;
  ariaLabel?: string; // Obligatorio para a11y, por defecto "Cerrar"
  onDismiss?: () => void;
}
```

## 3. ♿ Reglas de Accesibilidad (a11y) & Estados
- **Nombre Accesible Obligatorio:** Debe incluir siempre `aria-label="Cerrar"` (o texto traducido contextualmente ej. "Cerrar diálogo", "Cerrar alerta").
- **Hitbox Interactivo:** Aunque el icono visual mida 16-20px, el área de contacto táctil mediante padding o pseudoelemento debe alcanzar mínimo **44x44px** en dispositivos móviles (WCAG 2.5.5).
- **Focus Ring:** Debe disponer de indicador visible de foco (`:focus-visible`) con outline mínimo de 2px o 3px sin solapamiento.
- **Estados:** Default, Hover (`opacity: 0.75`), Active (`transform: scale(0.95)`), Disabled (`opacity: 0.25`, `pointer-events: none`).
