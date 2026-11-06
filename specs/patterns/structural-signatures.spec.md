# SPEC: Atomic Taxonomy & DOM Fingerprint Signatures

Reglas heurísticas para clasificar elementos DOM escaneados dentro de la jerarquía atómica (Atomic Design), superando la limitación de etiquetas nativas hacia la intención visual y roles computados.

---

## ⚛️ 1. ÁTOMOS (Atoms)
- **Profundidad DOM:** Nivel `<= 2` (ej. contenedor con texto, svg o imagen).
- **Firmas Heurísticas Específicas:**
  - **`atom-button` (Polimórfico):**
    - Todo `<button>` nativo o `<input type="button|submit">`.
    - **Enlaces de Acción (`<a>`):** Elementos `<a>` con propiedades computadas de botón:
      1. `display: inline-flex | flex | inline-block` con padding simétrico.
      2. Presencia de `border` visible (`borderWidth >= 2px`).
      3. Presencia de sombra o elevación (`boxShadow != none` o `.neo-shadow*`).
      4. Altura mínima interactiva (`min-height >= 44px` o `minHeight >= 36px`).
      5. Clases de acción (`.neo-hover`, `.btn`, `.btn-*`, `bg-primary`, `bg-secondary`, `font-bold`, mayúsculas).
      6. Ubicación en `<header>`, `<nav>` o bloques de call-to-action (`hero`, formularios).
  - **`atom-badge` / Chip:** Elementos `<span>` o `<div>` compactos (`font-size <= 12px`, texto en mayúsculas, fondo contrastante o píldora) usados como etiquetas temáticas (ej. `MARKETPLACE / UX RESEARCH`, `SEO / WEB DESIGN`).
  - **`atom-form-input`:** `<input>` de texto/email/password/textarea independientes.
  - **`atom-checkbox-radio`:** `<input type="checkbox|radio">` unitarios.

---

## 🧪 2. MOLÉCULAS (Molecules)
- **Profundidad DOM:** Nivel `3 - 5`.
- **Composición:** Agrupa entre 2 y 5 Átomos con un propósito funcional único.
- **Firmas Heurísticas Específicas:**
  - **`molecule-metric-card` / Case Study Card:**
    - Contenedor con borde grueso (`border-4` a `border-8`) y sombra dura (`translate-x-6 translate-y-6`).
    - Compuesta por: `atom-badge` (categoría) + encabezado `<h3>` + párrafo descriptivo + `atom-button` o enlace de acción (`VER EL PROYECTO →`) + media container (imagen o iframe embed).
  - **`molecule-input-group`:** `<input>` acoplado a etiquetas prefijo/sufijo o botones adjuntos.
  - **`molecule-combobox`:** Input con dropdown flotante y lista de opciones.
  - **`molecule-otp-input`:** Conjunto horizontal de 4-8 inputs unitarios.
  - **`molecule-password-strength`:** Input de contraseña + toggle de visibilidad + medidor de fortaleza.
  - **`molecule-datepicker`:** Input + popover de grilla de calendario.

---

## 🧬 3. ORGANISMOS (Organisms)
- **Profundidad DOM:** Nivel `> 5`.
- **Composición:** Múltiples Moléculas y Átomos heterogéneos organizados en layouts bi-dimensionales.
- **Firmas Heurísticas Específicas:**
  - `<header>` con logo y barra de navegación (`nav`).
  - Grillas de proyectos (`#work` con bento-grid de múltiples `molecule-metric-card`).
  - Tablas con filtros interactivos (`organism-data-table-slicer`).
  - Árboles de jerarquía (`organism-ai-decomposition-tree`).
  - Pie de página (`<footer>`) con enlaces, créditos y copyright.
