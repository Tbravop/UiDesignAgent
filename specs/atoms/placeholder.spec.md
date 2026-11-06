# SPEC: AtomPlaceholder (Skeleton & Placeholder Loader Contract)

## 1. 🎯 Fingerprint & Heuristic Matching
- **DOM Signatures:**
  - Bloques geométricos grises o desaturados con dimensiones simuladas de texto o imágenes (`height: 1em`, `width: 50%`, etc.), con animación de parpadeo (`animation: placeholder-glow`) o efecto shimmer/ola (`animation: placeholder-wave`).
  - Firmas de clases utilitarias de referencia: `.placeholder`, `.placeholder-glow`, `.placeholder-wave`, `.placeholder-xs|sm|lg`.
  - Usado para mitigar el Cumulative Layout Shift (CLS) durante cargas diferidas de interfaces.

## 2. 📐 Component Interface & Props
```typescript
export type PlaceholderAnimation = 'glow' | 'wave' | 'none';
export type PlaceholderSize = 'xs' | 'sm' | 'md' | 'lg';

export interface PlaceholderProps {
  width?: string | number; // ej. "75%", 120
  height?: string | number;
  animation?: PlaceholderAnimation;
  size?: PlaceholderSize;
  className?: string;
  isCircle?: boolean; // Para avatars o thumbnails
}
```

## 3. ♿ Reglas de Accesibilidad (a11y) & Estados
- **Ocultamiento a Tecnologías de Asistencia:** Todo placeholder debe incluir `aria-hidden="true"` para evitar que los lectores de pantalla anuncien elementos vacíos o basura textual.
- **Contenedor con `aria-busy`:** El componente o sección padre que está cargando el contenido debe declarar `aria-busy="true"` mientras los placeholders estén visibles.
- **Movimiento Reducido:** Detener el efecto de onda/brillo continuo bajo `prefers-reduced-motion: reduce`.
