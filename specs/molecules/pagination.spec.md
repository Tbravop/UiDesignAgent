# SPEC: MoleculePagination (Pagination Navigation Contract)

## 1. 🎯 Fingerprint & Heuristic Matching
- **DOM Signatures:**
  - Contenedor semántico `<nav aria-label="Paginación">` con lista horizontal `<ul class="pagination">` que agrupa botones numéricos de página y botones de anterior (`Previous` / `«`) y siguiente (`Next` / `»`).
  - Firmas de clases utilitarias de referencia: `.pagination`, `.page-item`, `.page-link`, `.pagination-sm|lg`.
  - La página actual se distingue visualmente con fondo contrastante (`.active`).

## 2. 📐 Component Interface & Props
```typescript
export interface PaginationProps {
  currentPage: number;
  totalPages: number;
  onPageChange: (page: number) => void;
  siblingCount?: number; // Páginas mostradas a cada lado de la actual (por defecto 1 o 2)
  showFirstLast?: boolean;
  size?: 'sm' | 'md' | 'lg';
  ariaLabel?: string;
}
```

## 3. ♿ Reglas de Accesibilidad (a11y) & Estados
- **Semántica:** Envoltura en `<nav aria-label="{ariaLabel || 'Paginación'}">`.
- **Página Activa:** El botón de la página actual debe tener obligatoriamente `aria-current="page"`.
- **Botones de Navegación:** Los controles anterior/siguiente deben llevar etiquetas textuales audibles mediante `aria-label="Ir a la página anterior"` y `"Ir a la página siguiente"`.
- **Estados Deshabilitados:** Cuando `currentPage === 1`, el botón de retroceso debe reflejar `aria-disabled="true"`, `tabIndex={-1}` y deshabilitación visual.
- **Hitbox:** Cada botón de página debe tener un área táctil mínima de **44x44px**.
