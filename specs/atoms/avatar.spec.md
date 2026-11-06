# Spec: Atom — Avatar (`atom-avatar`)

Representación visual de un usuario, autor o entidad mediante imagen de perfil, iniciales de respaldo (fallback) e indicador opcional de estado en línea.

---

## 1. 🎯 Fingerprint & Heuristic Matching

- **Selectores Semánticos / Estructurales:** `<figure>`, `<span>` o `<div>` con `aspect-ratio: 1 / 1` que envuelve un `<img>` (`object-fit: cover`) o un nodo de texto corto (1 a 3 caracteres en mayúsculas).
- **Heurística de Caja (Playwright):**
  - Relación de aspecto cuadrada (`width === height`, típicamente `32px`, `40px`, `48px` o `64px`).
  - `overflow: hidden` en el contenedor de imagen y borde sólido del sistema (`2px` o `3px` en Neo-Memphis).
  - En agrupaciones (`AvatarGroup`), los elementos hermanos presentan margen negativo (`margin-left: -8px`) y borde de recorte del color de superficie.

---

## 2. 📐 Component Interface & Props

```typescript
export interface AvatarProps {
  /** URL de la imagen de perfil */
  src?: string;
  /** Texto alternativo obligatorio si existe imagen, o nombre completo para derivar iniciales */
  alt: string;
  /** Iniciales de respaldo cuando la imagen falla o no está disponible (ej. 'TB') */
  fallbackInitials: string;
  /** Escala de tamaño en grilla de 4px */
  size?: 'sm' | 'md' | 'lg' | 'xl'; // 32px | 40px | 48px | 64px
  /** Forma geométrica según los tokens de DESIGN.md */
  shape?: 'square' | 'circle';
  /** Indicador semántico de presencia */
  status?: 'online' | 'busy' | 'offline';
}
```

### Mapeo a Tokens de `./DESIGN.md`
- **Fondo de Fallback:** `--color-secondary` (`oklch(0.69 0.14 275)`) o `--color-accent-yellow` con texto `--color-on-surface`.
- **Borde:** `2px solid var(--color-on-surface)` y sombra dura opcional `2px 2px 0px var(--color-on-surface)`.

---

## 3. ♿ Reglas de Accesibilidad (a11y) & Estados

- **Imagen con Significado:** El atributo `alt` debe describir a la persona o entidad (ej. `alt="Tomás Bravo"`). Si el avatar acompaña inmediatamente al nombre visible en texto plano, puede usar `alt=""` y `aria-hidden="true"` para evitar redundancia en lectores de pantalla.
- **Respaldo Resiliente (`onerror`):** Si la carga de `src` falla, se oculta el nodo `<img>` y se muestra el contenedor de `fallbackInitials` con contraste mínimo **4.5:1**.
- **Indicador de Estado:** Si `status` está definido, el punto visual debe incluir un `<span class="sr-only">` con el estado textual (`"En línea"`, `"Ocupado"`, `"Desconectado"`).
