# SPEC: OrganismCarousel (Image & Content Carousel Slider Contract)

## 1. 🎯 Fingerprint & Heuristic Matching
- **DOM Signatures:**
  - Contenedor dinámico deslizante (`.carousel`) que contiene una tira de diapositivas (`.carousel-inner`, `.carousel-item`), indicadores de posición de puntos o barras (`.carousel-indicators`), y botones de control previo/siguiente (`.carousel-control-prev`, `.carousel-control-next`).
  - Firmas de clases utilitarias de referencia: `.carousel`, `.carousel-inner`, `.carousel-item`, `.carousel-control-prev`, `.carousel-control-next`, `.carousel-indicators`, `.carousel-fade`.

## 2. 📐 Component Interface & Props
```typescript
export interface CarouselSlide {
  id: string;
  imageSrc: string;
  imageAlt: string;
  title?: string;
  caption?: string;
  linkHref?: string;
}

export interface CarouselProps {
  slides: CarouselSlide[];
  autoPlay?: boolean;
  interval?: number; // en ms (por defecto 5000ms)
  showIndicators?: boolean;
  showControls?: boolean;
  pauseOnHover?: boolean;
  isFade?: boolean;
}
```

## 3. ♿ Reglas de Accesibilidad (a11y) & Estados
- **Patrón WAI-ARIA Carousel:**
  - Contenedor con `role="region"` y `aria-roledescription="carrusel"` con `aria-label="Galería de proyectos destacados"`.
  - Cada diapositiva debe tener `role="group"`, `aria-roledescription="diapositiva"` y `aria-label={`{index + 1} de {total}`}`.
- **Botón de Pausa Obligatorio (WCAG 2.2.2 Pause, Stop, Hide):** Si el carrusel avanza automáticamente, debe incluir un botón de pausa/reproducción accesible por teclado o detenerse automáticamente cuando recibe foco (`:focus-within`) o puntero (`:hover`).
- **Preferencia de Movimiento:** Si `prefers-reduced-motion: reduce` está activo, deshabilitar la transición deslizante continua y el autoplay.
