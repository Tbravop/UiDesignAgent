# SPEC: MoleculeBreadcrumb (Breadcrumb Navigation Trail Contract)

## 1. 🎯 Fingerprint & Heuristic Matching
- **DOM Signatures:**
  - Contenedor semántico `<nav aria-label="breadcrumb">` conteniendo una lista ordenada `<ol class="breadcrumb">` con elementos `<li>` separados por divisores tipo `/`, `>` o chevrons.
  - El último elemento corresponde a la página actual sin enlace activo (`aria-current="page"`).
  - Firmas de clases utilitarias de referencia: `.breadcrumb`, `.breadcrumb-item`.

## 2. 📐 Component Interface & Props
```typescript
export interface BreadcrumbItem {
  label: string;
  href?: string;
  isCurrent?: boolean;
}

export interface BreadcrumbProps {
  items: BreadcrumbItem[];
  separator?: React.ReactNode; // Por defecto "/" o chevron
  ariaLabel?: string;
}
```

## 3. ♿ Reglas de Accesibilidad (a11y) & Estados
- **Semántica Estricta:**
  - Debe usar `<nav aria-label="Breadcrumb">` para que los lectores de pantalla anuncien la región de migas de pan.
  - El ítem de la página actual debe tener obligatoriamente `aria-current="page"`.
- **Separadores Ocultos:** Los caracteres divisores (ej. `/`) deben insertarse mediante CSS (`::before`) o marcarse con `aria-hidden="true"` para que no se lean como texto fonético innecesario.
- **Hitbox:** Cada enlace de la ruta debe contar con un área interactiva cómoda de mínimo **44px** en mobile.
