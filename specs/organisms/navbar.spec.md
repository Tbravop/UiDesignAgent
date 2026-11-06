# SPEC: OrganismNavbar (Responsive Header Navigation Bar Contract)

## 1. 🎯 Fingerprint & Heuristic Matching
- **DOM Signatures:**
  - Cabecera fija o adhesiva (`<header>` o `<nav class="navbar">`) ubicada en la parte superior de la página, que agrupa logotipo de marca (`.navbar-brand`), enlaces de navegación (`.nav-link`), botón hamburguesa de colapso en pantallas móviles (`.navbar-toggler`), y botones de acción primaria (`atom-button`).
  - Firmas de clases utilitarias de referencia: `.navbar`, `.navbar-brand`, `.navbar-toggler`, `.navbar-collapse`, `.navbar-nav`, `.sticky-top`, `.fixed-top`.
  - En el portafolio: `<header class="sticky top-0 w-full z-[100] ...">` con logo `Bravo!` y enlaces con `min-h-[44px]`.

## 2. 📐 Component Interface & Props
```typescript
export interface NavItem {
  id: string;
  label: string;
  href: string;
  isActive?: boolean;
  isButton?: boolean;
  buttonVariant?: 'primary' | 'secondary' | 'surface';
}

export interface NavbarProps {
  brand: React.ReactNode;
  brandHref?: string;
  items: NavItem[];
  actions?: React.ReactNode;
  isSticky?: boolean;
  isTransparent?: boolean;
}
```

## 3. ♿ Reglas de Accesibilidad (a11y) & Estados
- **Semántica:** Envoltura en `<header>` y bloque `<nav aria-label="Navegación principal">`.
- **Botón Hamburguesa (`.navbar-toggler`):**
  - Debe contener `aria-label="Abrir menú de navegación"`, `aria-expanded="true|false"` y `aria-controls="{nav-collapse-id}"`.
- **Enlace Activo:** El ítem correspondiente a la sección o página actual debe tener `aria-current="page"`.
- **Hitbox:** Todos los enlaces y botones de navegación deben tener un tamaño táctil mínimo de **44x44px** (WCAG 2.5.5).
- **Saltar al Contenido:** Debe coexistir con un enlace de salto de accesibilidad inicial `<a href="#main-content" class="sr-only focus:not-sr-only">`.
