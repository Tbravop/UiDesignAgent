# SPEC: AtomButton (Button & Action Link Contract)

## 1. 🎯 Fingerprint & Heuristic Matching
- **DOM Signatures:**
  - Etiquetas `<button>` nativas o `<input type="button|submit">`.
  - Elementos `<a>` con `href` estilizados con bordes, sombras duras (`box-shadow`), altura mínima (`min-height >= 44px`), `display: inline-flex | inline-block`, padding de caja y estados hover/active de acción (ej. botones del `<header>`, botón "Contrátame", botones de hero).
  - Elementos con atributo explícito `role="button"`.
- **Heurística de Desacoplamiento:** Mapea selectores tipo `.btn`, `.btn-*`, `.neo-btn`, `.neo-hover` a un componente unificado y agnóstico.

## 2. 📐 Component Interface & Props
```typescript
export type ButtonVariant = 'primary' | 'secondary' | 'tertiary' | 'outline' | 'ghost' | 'danger';
export type ButtonSize = 'sm' | 'md' | 'lg';

export interface ButtonBaseProps {
  variant?: ButtonVariant;
  size?: ButtonSize;
  isIconOnly?: boolean;
  leftIcon?: React.ReactNode;
  rightIcon?: React.ReactNode;
  isLoading?: boolean;
  isDisabled?: boolean;
  fullWidth?: boolean;
}

// Soporte Polimórfico (Botón nativo o Enlace de Acción <a>)
export type ButtonProps = ButtonBaseProps & (
  | ({ as?: 'button' } & React.ButtonHTMLAttributes<HTMLButtonElement>)
  | ({ as: 'a'; href: string } & React.AnchorHTMLAttributes<HTMLAnchorElement>)
);
```

## 3. ♿ Reglas de Accesibilidad (a11y) & Estados
- **Hitbox Táctil:** Altura y anchura mínima interactiva de **44x44px** según WCAG 2.1 AA (criterio 2.5.5 Target Size).
- **Contraste de Color:** Mínimo ratio **4.5:1** para texto normal y **3:1** para bordes interactivos contra el fondo (`oklch`).
- **Estados Requeridos:**
  - `Default`: Reposo con elevación o sombra estándar (`6px 6px 0px var(--shadow-color)`).
  - `Hover`: Traslación y elevación aumentada (`translate(-3px, -3px)`).
  - `Active`: Simulación física de pulsado (`translate(2px, 2px)`).
  - `Focus-Visible`: Outline de 3px con separación (`outline-offset: 4px`), nunca omitir `:focus-visible`.
  - `Disabled`: `aria-disabled="true"`, `opacity: 0.5`, sin eventos de puntero (`pointer-events: none`).
- **Lectores de Pantalla:** `aria-label` mandatorio cuando `isIconOnly={true}`. Si se renderiza como `<a>` sin navegación (`href="#"`), debe incluir `role="button"` y `onKeyDown` para activar con tecla `Space`.
