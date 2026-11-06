# COMPONENTS.md — Registro del Sistema de Diseño (Universal & Agnostic Catalog)

Catálogo de componentes UI, Formularios y Data Viz mapeados a sus especificaciones en `./specs/` y modularizados en `./src/components/`.

---

## ⚛️ Atoms

### `atom-button`
* **spec_ref:** `./specs/atoms/button.spec.md`
* **code_ref:** `./src/components/atoms/button/button.html` & `./src/components/atoms/button/button.css`
* **descripción:** Botón polimórfico (`<button>` o `<a>`) con hitbox accesible de 44px, variantes (`primary`, `secondary`, `tertiary`, `surface`) y sombras Neo-Brutalistas.
* **status:** `Audited & Modularized from real DOM`

### `atom-badge`
* **spec_ref:** `./specs/atoms/badge.spec.md`
* **code_ref:** `./src/components/atoms/badge/badge.html` & `./src/components/atoms/badge/badge.css`
* **descripción:** Indicadores de estado y categorías temáticas con rotación sutil Memphis (`tilt-left`).
* **status:** `Audited & Modularized from real DOM`

### `atom-chip`
* **spec_ref:** `./specs/atoms/chip.spec.md`
* **code_ref:** `./src/components/atoms/chip/chip.html` & `./src/components/atoms/chip/chip.css`
* **descripción:** Píldoras de habilidades y filtros con bordes de 4px y sombra de elevación.
* **status:** `Audited & Modularized from real DOM`

### `atom-close-button`
* **spec_ref:** `./specs/atoms/close-button.spec.md`
* **descripción:** Botón de descarte accesible con `aria-label="Cerrar"` y hitbox mínimo de 44px.
* **status:** `Spec Defined (Agnostic Design Spec)`

### `atom-form-input`
* **spec_ref:** `./specs/atoms/form-input.spec.md`
* **descripción:** Campos de entrada de texto, email, búsqueda y textarea con estados de validación y contraste WCAG AA.
* **status:** `Spec Defined (Agnostic Form Spec)`

### `atom-checkbox-radio`
* **spec_ref:** `./specs/atoms/checkbox-radio.spec.md`
* **descripción:** Controles de selección booleana, opciones exclusivas y switches con hitbox mínimo de 44px.
* **status:** `Spec Defined (Agnostic Form Spec)`

### `atom-range`
* **spec_ref:** `./specs/atoms/range.spec.md`
* **descripción:** Control deslizante de rango horizontal con valores ARIA y thumb accesible de 44px.
* **status:** `Spec Defined (Agnostic Form Spec)`

### `atom-progress`
* **spec_ref:** `./specs/atoms/progress.spec.md`
* **descripción:** Barra de progreso accesible (`role="progressbar"`) con soporte de rayas y contraste mínimo 3:1.
* **status:** `Spec Defined (Agnostic Design Spec)`

### `atom-spinner`
* **spec_ref:** `./specs/atoms/spinner.spec.md`
* **descripción:** Indicador de carga animado circular o pulsante con texto para lectores de pantalla (`role="status"`).
* **status:** `Spec Defined (Agnostic Design Spec)`

### `atom-placeholder`
* **spec_ref:** `./specs/atoms/placeholder.spec.md`
* **descripción:** Skeletons de carga diferida con `aria-hidden="true"` para mitigar el Cumulative Layout Shift (CLS).
* **status:** `Spec Defined (Agnostic Design Spec)`

### `atom-avatar`
* **spec_ref:** `./specs/atoms/avatar.spec.md`
* **descripción:** Imagen de perfil cuadrada o circular (`aspect-ratio: 1/1`) con iniciales de respaldo (`fallbackInitials`) e indicador de estado accesible.
* **status:** `Spec Defined (Agnostic Design Spec)`

### `atom-separator`
* **spec_ref:** `./specs/atoms/separator.spec.md`
* **descripción:** Divisor semántico horizontal o vertical (`<hr>` o `role="separator"`) alineado a la grilla de 4px y grosor de trazo del sistema.
* **status:** `Spec Defined (Agnostic Design Spec)`

---

## 🧪 Molecules (UI & Data Viz)

### `molecule-card` / `molecule-metric-card`
* **spec_ref:** `./specs/molecules/card.spec.md` & `./specs/molecules/metric-card.spec.md`
* **code_ref:** `./src/components/molecules/card/card.html` & `./src/components/molecules/card/card.css`
* **descripción:** Tarjeta horizontal dividida en 2 columnas (slot media 34% + slot contenido jerárquico 53%) con borde de 8px y sombra física.
* **status:** `Audited & Modularized from real DOM`

### `molecule-button-group`
* **spec_ref:** `./specs/molecules/button-group.spec.md`
* **code_ref:** `./src/components/molecules/button-group/button-group.html` & `./src/components/molecules/button-group/button-group.css`
* **descripción:** Barra de botones de filtro por categoría con estado activo `aria-pressed="true|false"`.
* **status:** `Audited & Modularized from real DOM`

### `molecule-marquee`
* **spec_ref:** `./specs/molecules/marquee.spec.md`
* **code_ref:** `./src/components/molecules/marquee/marquee.html` & `./src/components/molecules/marquee/marquee.css`
* **descripción:** Banda cinética horizontal de desplazamiento continuo detectada por Playwright (`Auto-Spec Discovery`) con pausa en hover y soporte `prefers-reduced-motion`.
* **status:** `Auto-Spec Generated & Modularized from real DOM`

### `molecule-alert`
* **spec_ref:** `./specs/molecules/alert.spec.md`
* **descripción:** Notificación contextual en bloque con variantes de color, icono y botón de descarte opcional.
* **status:** `Spec Defined (Agnostic Design Spec)`

### `molecule-breadcrumb`
* **spec_ref:** `./specs/molecules/breadcrumb.spec.md`
* **descripción:** Ruta de navegación jerárquica con `<nav aria-label="Breadcrumb">` y `aria-current="page"`.
* **status:** `Spec Defined (Agnostic Design Spec)`

### `molecule-dropdown`
* **spec_ref:** `./specs/molecules/dropdown.spec.md`
* **descripción:** Menú contextual desplegable flotante bajo el estándar WAI-ARIA Menu Button navegable con flechas.
* **status:** `Spec Defined (Agnostic Design Spec)`

### `molecule-list-group`
* **spec_ref:** `./specs/molecules/list-group.spec.md`
* **descripción:** Lista vertical con divisores continuos, soporte de enlaces activos y badges de conteo.
* **status:** `Spec Defined (Agnostic Design Spec)`

### `molecule-pagination`
* **spec_ref:** `./specs/molecules/pagination.spec.md`
* **descripción:** Controles de paginación numérica con etiquetas audibles y `aria-current="page"`.
* **status:** `Spec Defined (Agnostic Design Spec)`

### `molecule-popover`
* **spec_ref:** `./specs/molecules/popover.spec.md`
* **descripción:** Superposición flotante con título y contenido enriquecido mediante `role="dialog"`.
* **status:** `Spec Defined (Agnostic Design Spec)`

### `molecule-tooltip`
* **spec_ref:** `./specs/molecules/tooltip.spec.md`
* **descripción:** Información emergente contextual en hover/focus con soporte de cierre vía `Escape` (WCAG 1.4.13).
* **status:** `Spec Defined (Agnostic Design Spec)`

### `molecule-toast`
* **spec_ref:** `./specs/molecules/toast.spec.md`
* **descripción:** Notificación flotante de confirmación o alerta con live region y botón de cierre.
* **status:** `Spec Defined (Agnostic Design Spec)`

### `molecule-hover-card`
* **spec_ref:** `./specs/molecules/hover-card.spec.md`
* **descripción:** Tarjeta flotante no bloqueante de previsualización enriquecida en `:hover` y `:focus-visible`.
* **status:** `Spec Defined (Agnostic Design Spec)`

### `molecule-context-menu`
* **spec_ref:** `./specs/molecules/context-menu.spec.md`
* **descripción:** Menú contextual desplegado en las coordenadas de clic secundario (`contextmenu`) con navegación WAI-ARIA Menu.
* **status:** `Spec Defined (Agnostic Design Spec)`

### `molecule-floating-label`
* **spec_ref:** `./specs/molecules/floating-label.spec.md`
* **descripción:** Campo de formulario con etiqueta flotante que asciende al enfocar o ingresar texto.
* **status:** `Spec Defined (Agnostic Form Spec)`

### `molecule-input-group`
* **spec_ref:** `./specs/molecules/input-group.spec.md`
* **descripción:** Fusión de input con addons de texto o botones de acción colapsando bordes interiores.
* **status:** `Spec Defined (Agnostic Form Spec)`

### `molecule-combobox`
* **spec_ref:** `./specs/molecules/combobox.spec.md`
* **descripción:** Selector avanzado con búsqueda, autocompletado y menú listbox accesible (WAI-ARIA 1.2).
* **status:** `Spec Defined (Agnostic Form Spec)`

### `molecule-otp-input`
* **spec_ref:** `./specs/molecules/otp-input.spec.md`
* **descripción:** Entrada de códigos de verificación de 4 a 8 casillas con avance automático y soporte de pegado.
* **status:** `Spec Defined (Security Form Spec)`

### `molecule-password-strength`
* **spec_ref:** `./specs/molecules/password-strength.spec.md`
* **descripción:** Input de contraseña con toggle de visibilidad y medidor dinámico de seguridad (`role="status"`).
* **status:** `Spec Defined (Security Form Spec)`

### `molecule-datepicker`
* **spec_ref:** `./specs/molecules/datepicker.spec.md`
* **descripción:** Input selector de fechas con calendario popover navegable por teclado.
* **status:** `Spec Defined (Date Form Spec)`

### `molecule-bar-column-chart`
* **spec_ref:** `./specs/molecules/bar-column-chart.spec.md`
* **descripción:** Gráficos de barras y columnas con tabla accesible `sr-only` y tokens de series OKLCH.
* **status:** `Spec Defined (DataViz Catalog)`

### `molecule-line-area-chart`
* **spec_ref:** `./specs/molecules/line-area-chart.spec.md`
* **descripción:** Tendencias temporales en SVG con hitbox interactivo mínimo de 44px en puntos.
* **status:** `Spec Defined (DataViz Catalog)`

### `molecule-proportion-chart`
* **spec_ref:** `./specs/molecules/proportion-chart.spec.md`
* **descripción:** Gráficos de anillo y pastel para distribución proporcional.
* **status:** `Spec Defined (DataViz Catalog)`

### `molecule-gauge-map`
* **spec_ref:** `./specs/molecules/gauge-map.spec.md`
* **descripción:** Medidor semicircular de cumplimiento de metas y SLAs.
* **status:** `Spec Defined (DataViz Catalog)`

---

## 🧬 Organisms (UI & Data Viz)

### `organism-navbar`
* **spec_ref:** `./specs/organisms/navbar.spec.md`
* **code_ref:** `./src/components/organisms/navbar/navbar.html` & `./src/components/organisms/navbar/navbar.css`
* **descripción:** Barra de navegación sticky con logotipo de marca, enlaces de acción y hitboxes accesibles de 44px.
* **status:** `Audited & Modularized from real DOM`

### `organism-accordion`
* **spec_ref:** `./specs/organisms/accordion.spec.md`
* **descripción:** Paneles colapsables apilados con encabezados accesibles y control por teclado.
* **status:** `Spec Defined (Agnostic Design Spec)`

### `organism-carousel`
* **spec_ref:** `./specs/organisms/carousel.spec.md`
* **descripción:** Carrusel de diapositivas con controles de pausa obligatorios y soporte `prefers-reduced-motion`.
* **status:** `Spec Defined (Agnostic Design Spec)`

### `organism-modal`
* **spec_ref:** `./specs/organisms/modal.spec.md`
* **descripción:** Diálogo emergente con trampa de foco (`focus trap`), bloqueo de fondo y cierre con `Escape`.
* **status:** `Spec Defined (Agnostic Design Spec)`

### `organism-navs-tabs`
* **spec_ref:** `./specs/organisms/navs-tabs.spec.md`
* **descripción:** Interfaz de pestañas (`role="tablist"`, `role="tab"`, `role="tabpanel"`) navegable con flechas.
* **status:** `Spec Defined (Agnostic Design Spec)`

### `organism-offcanvas`
* **spec_ref:** `./specs/organisms/offcanvas.spec.md`
* **descripción:** Panel lateral deslizable para menús móviles o filtros con trampa de foco y backdrop.
* **status:** `Spec Defined (Agnostic Design Spec)`

### `organism-command-palette`
* **spec_ref:** `./specs/organisms/command-palette.spec.md`
* **descripción:** Centro omnibox modal de búsqueda y ejecución rápida de comandos (`role="dialog"` + `role="combobox"`).
* **status:** `Spec Defined (Agnostic Design Spec)`

### `organism-data-table-slicer`
* **spec_ref:** `./specs/organisms/data-table-slicer.spec.md`
* **descripción:** Tabla de datos con filtros en píldoras, ordenamiento y desplazamiento responsivo.
* **status:** `Spec Defined (DataViz Catalog)`

### `organism-ai-decomposition-tree`
* **spec_ref:** `./specs/organisms/ai-decomposition-tree.spec.md`
* **descripción:** Árbol jerárquico de decisión con nodos colapsables y líneas conectoras.
* **status:** `Spec Defined (DataViz Catalog)`
