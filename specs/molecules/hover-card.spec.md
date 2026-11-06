# Spec: Molecule — Hover Card (`molecule-hover-card`)

Tarjeta flotante contextual no bloqueante que permite previsualizar información enriquecida detrás de un enlace o referencia al posar el puntero o enfocar con teclado.

---

## 1. 🎯 Fingerprint & Heuristic Matching

- **Selectores Semánticos / Estructurales:** Un disparador (`<a>` o `<button>`) vinculado mediante `aria-describedby` o contenedor relativo a un panel flotante (`position: absolute | fixed`, `z-index >= 40`) que contiene resumen, avatar o metadatos.
- **Heurística de Caja (Playwright):**
  - Permanece oculto en reposo (`display: none` o `opacity: 0; pointer-events: none`) y se despliega tras un retardo de intención (`openDelay: ~200ms`) en `:hover` o `:focus-within`.
  - Ancho acotado (`280px` a `360px`), borde de contenedor de `3px` y sombra dura desplazada.

---

## 2. 📐 Component Interface & Props

```typescript
export interface HoverCardProps {
  /** Identificador único para vincular el disparador con el panel */
  id: string;
  /** Posición preferida respecto al elemento disparador */
  placement?: 'top' | 'bottom' | 'left' | 'right';
  /** Retardo de apertura en milisegundos para evitar parpadeos accidentales */
  openDelay?: number;
  /** Retardo de cierre en milisegundos para permitir mover el cursor al panel */
  closeDelay?: number;
}
```

### Mapeo a Tokens de `./DESIGN.md`
- **Superficie:** `--color-surface-card` (`oklch(1.00 0 0)`) con borde `3px solid var(--color-on-surface)` y sombra `--shadow-hard-md` (`6px 6px 0px`).
- **Padding Interno:** `16px` (`1rem`) con separación interna de `8px`.

---

## 3. ♿ Reglas de Accesibilidad (a11y) & Estados

- **Paridad Teclado / Puntero:** El panel debe abrirse tanto con `:hover` como con `:focus-visible` sobre el disparador, y cerrarse al presionar la tecla `Escape`.
- **No Trampa de Foco:** A diferencia de un modal (`organism-modal`), el Hover Card nunca atrapa el foco ni bloquea el scroll de la página; su contenido es complementario.
- **Movimiento Reducido:** Con `prefers-reduced-motion: reduce`, la aparición es instantánea sin transiciones de traslación.
