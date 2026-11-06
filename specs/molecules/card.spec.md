# SPEC: MoleculeCard (Content & Media Card Container Contract)

## 1. 🎯 Fingerprint & Heuristic Matching
- **DOM Signatures:**
  - Contenedor rectangular con borde, sombra o elevación definida, estructurado típicamente en cabecera (`.card-header`), cuerpo con padding (`.card-body`), imagen superior/inferior (`.card-img-top`) y pie (`.card-footer`).
  - Firmas de clases utilitarias de referencia: `.card`, `.card-body`, `.card-title`, `.card-text`, `.card-header`, `.card-footer`, `.card-img`.
  - Típico en catálogos de productos, perfiles de usuario, resúmenes de artículos y dashboards.

## 2. 📐 Component Interface & Props
```typescript
export interface CardProps {
  header?: React.ReactNode;
  footer?: React.ReactNode;
  imageSrc?: string;
  imageAlt?: string;
  imagePosition?: 'top' | 'bottom' | 'overlay';
  title?: string;
  subtitle?: string;
  children: React.ReactNode;
  isHoverable?: boolean;
  isClickable?: boolean;
  onClick?: () => void;
  className?: string;
}
```

## 3. ♿ Reglas de Accesibilidad (a11y) & Estados
- **Semántica:** Si representa una unidad de contenido autocontenida que puede redistribuirse, debe renderizarse con `<article>`. Si es un contenedor de agrupación general, usar `<div>` o `<section aria-labelledby="{id}">`.
- **Accesibilidad de Imágenes:** Toda imagen decorativa debe tener `alt=""`; imágenes informativas deben describir con precisión su contenido.
- **Tarjetas Clickeables:** Si la tarjeta entera redirige a una URL, se recomienda usar el patrón de enlace expandido (el `<a>` principal dentro del título expande su área clicable a toda la tarjeta mediante `::after` absoluto) para evitar anidar botones dentro de enlaces interactivos inválidos.
