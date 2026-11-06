# UXAGENT.md: Guía Genérica para el Agente de Desarrollo Frontend

Esta es una guía de descubrimiento, cadencia y arquitectura para agentes de IA encargados de modificar o crear código en el repositorio frontend. El objetivo es evitar el error más común de las IA: generar código antes de investigar lo que ya existe.

---

## 📍 Resolución de Rutas y Portabilidad Multi-Proyecto

Este kit de directivas y skills está diseñado para ejecutarse de forma portátil en **cualquier proyecto**:
- **Ubicación de este Kit:** Puede ubicarse en la raíz del repositorio (`./`), dentro de un subdirectorio (ej. `./UXAgent/`, `./.agents/`, `./.gemini/`, `./tools/UXAgent/`) o en un directorio global de skills. Todas las referencias internas entre sus propios archivos son relativas (`./` o relativas entre carpetas de `skills/`).
- **`DESIGN.md` del Proyecto vs `DESIGN.md` de Plantilla:**
  - El archivo oficial de diseño de la aplicación es el que reside en la **raíz del proyecto anfitrión** (`<raíz-proyecto>/DESIGN.md`).
  - Si el proyecto aún no cuenta con su propio `DESIGN.md`, el agente debe usar el archivo [`DESIGN.md`](./DESIGN.md) de este kit como **plantilla y especificación base** para generarlo en la raíz del proyecto mediante [`skills/brand-identity-discovery/SKILL.md`](./skills/brand-identity-discovery/SKILL.md).
- **Detección Flexible en Monorepos y Multi-paquetes:** El agente debe buscar los archivos de configuración (`package.json`, configuraciones de estilos, etc.) tanto en la raíz del repositorio como en el subdirectorio específico del paquete frontend (ej. `apps/web/`, `frontend/`, `client/`, `packages/ui/`).

---

## 🗺️ Orquestación y Mapa de Skills del Agente

Antes de ejecutar cualquier cambio en el código, el agente debe activar y respetar las directrices de las skills especializadas y los documentos base según el ciclo de vida de la tarea:

| Documento / Skill | Ruta Relativa | Disparador (Trigger) / Propósito |
| :--- | :--- | :--- |
| **`UXAGENT.md`** | [`./UXAGENT.md`](./UXAGENT.md) | Orquestador principal, cadencia de verificación, reglas de arquitectura y flujo de ejecución. |
| **`DESIGN.md`** | [`./DESIGN.md`](./DESIGN.md) | Única fuente de verdad de tokens OKLCH, escala tipográfica `clamp()`, grid modular de 4px, hitboxes de 44x44px y motion. |
| **`COMPONENTS.md`** | [`./COMPONENTS.md`](./COMPONENTS.md) | Catálogo universal de especificaciones agnósticas (`.spec.md`) divididas en Átomos, Moléculas, Organismos y Patrones. |
| **`specs/`** | [`./specs/`](./specs/) | 48 contratos de componentes agnósticos (`atoms/`, `molecules/`, `organisms/`, `patterns/`) con heurísticas de Playwright, interfaces TypeScript y reglas WAI-ARIA. |
| **`brand-identity-discovery`** | [`./skills/brand-identity-discovery/SKILL.md`](./skills/brand-identity-discovery/SKILL.md) | Disparar al inicializar un repositorio sin `DESIGN.md` en su raíz, al integrar una nueva marca o migrar paletas a OKLCH. |
| **`framework-token-adapter`** | [`./skills/framework-token-adapter/SKILL.md`](./skills/framework-token-adapter/SKILL.md) | Disparar inmediatamente tras crear o modificar `DESIGN.md` para compilar tokens en Tailwind v3/v4 o CSS Modules. |
| **`design-system-auditor`** | [`./skills/design-system-auditor/SKILL.md`](./skills/design-system-auditor/SKILL.md) | Disparar al auditar un sitio con Playwright y antes de crear o estandarizar cualquier vista o componente UI (Regla 1). Prioriza la biblioteca nativa, corrige contraste/clases dispares en vistas y usa `./specs/` para componentes abstractos. |
| **`writing-ui-components`** | [`./skills/writing-ui-components/SKILL.md`](./skills/writing-ui-components/SKILL.md) | Disparar al crear, estructurar, dividir o mover componentes UI (Regla 5). Aplica la escalera de abstracción y estados obligatorios. |
| **`anti-patterns.md`** | [`./skills/writing-ui-components/references/anti-patterns.md`](./skills/writing-ui-components/references/anti-patterns.md) | Catálogo de malas prácticas y anti-patrones que deben corregirse a la vista en componentes, estilos y asincronía. |
| **`accessibility-contrast-auditor`** | [`./skills/accessibility-contrast-auditor/SKILL.md`](./skills/accessibility-contrast-auditor/SKILL.md) | Disparar al definir combinaciones de color, estados hover/focus, áreas táctiles mínimas (44x44px) y media queries de accesibilidad (Regla 6). |

---

## 🚀 Protocolo de Ejecución Obligatorio (Fase -1 a Fase 4)

Antes de modificar cualquier archivo de la aplicación, el agente DEBE seguir esta secuencia de ejecución:

0. **Fase -1 — Auto-Instalación e Inicialización de Playwright (Inspección en Vivo):**
   - Al auditar una interfaz web o servidor local, verificar disponibilidad: `python -c "import playwright"`.
   - Si no está instalado, instalar de forma desatendida:
     ```powershell
     python -m pip install playwright
     python -m playwright install chromium
     ```
   - Inspeccionar el DOM renderizado (`window.getComputedStyle`, `getBoundingClientRect`) en viewport `1440x900` para medir contrastes reales, hitboxes (`>= 44px`), bordes, sombras y consistencia de clases entre cajas hermanas.

1. **Fase 0 — Detección de Framework, Stack Técnico y Descubrimiento Recursivo de Vistas:**
   - El agente nunca debe asumir el stack, las librerías ni la estructura de carpetas del proyecto. Debe comenzar inspeccionando:
     - `package.json`: Buscar en la raíz del repositorio o dentro del paquete frontend correspondiente (`apps/*`, `packages/*`, `frontend/`, `client/`). Detectar framework base (React, Next.js, Vite, Vue, Svelte, Angular, Astro, etc.) y motor de estilos (Utility CSS, CSS Modules, Variables CSS, etc.).
     - Archivos de configuración: configuraciones de estilos, bundlers y compiladores.
     - Biblioteca de UI instalada: biblioteca de componentes o sistema de clases nativo del proyecto.
     - **Descubrimiento y Mapeo Recursivo de Vistas (`Deep View Discovery`):** Rastrear exhaustivamente todas las vistas del proyecto sin importar su nivel de profundidad o ubicación (`app/**/page.*`, `pages/**/*`, `views/**/*`, `scenes/**/*`, `features/**/pages/*`, `modules/**/views/*`, `templates/**/*.html` y enrutadores `routes.*`). Ninguna vista debe quedar sin auditar por estar dentro de subcarpetas o módulos de dominio.

2. **Fase 1 — Validación de Identidad y Tokens (`brand-identity-discovery`):**
   - Verificar si el proyecto cuenta con un `DESIGN.md` en su raíz (`<raíz-proyecto>/DESIGN.md`).
   - Si no existe, activar [`./skills/brand-identity-discovery/SKILL.md`](./skills/brand-identity-discovery/SKILL.md) para inspeccionar paletas o aplicar el arquetipo correspondiente y compilar `DESIGN.md` en la raíz del proyecto basándose en la plantilla [`./DESIGN.md`](./DESIGN.md).

3. **Fase 2 — Adaptación de Tokens al Framework (`framework-token-adapter`):**
   - Activar [`./skills/framework-token-adapter/SKILL.md`](./skills/framework-token-adapter/SKILL.md) para validar o inyectar las variables y tokens de `DESIGN.md` en la sintaxis nativa del motor de estilos detectado en la Fase 0 (Tailwind v3/v4 o CSS Modules/Variables).

4. **Fase 3 — Auditoría de Precedentes y Componentes (`design-system-auditor`):**
   - Antes de escribir o refactorizar cualquier pantalla, diálogo o formulario, activar [`./skills/design-system-auditor/SKILL.md`](./skills/design-system-auditor/SKILL.md) para inventariar componentes existentes y forzar la reutilización (Regla 1).

5. **Fase 4 — Construcción, Accesibilidad y Validación (`writing-ui-components` & `anti-patterns.md`):**
   - Construir interfaces aplicando la escalera de abstracción y los tres estados obligatorios según [`./skills/writing-ui-components/SKILL.md`](./skills/writing-ui-components/SKILL.md).
   - Garantizar contraste WCAG y áreas táctiles mínimas de 44x44px según [`./skills/accessibility-contrast-auditor/SKILL.md`](./skills/accessibility-contrast-auditor/SKILL.md).
   - Verificar el marcado final contra el catálogo de [`./skills/writing-ui-components/references/anti-patterns.md`](./skills/writing-ui-components/references/anti-patterns.md).

---

## Regla 1 — Reutilizar la Biblioteca Nativa y Estandarizar Activamente la Vista

Antes de compilar o programar cualquier elemento de la interfaz de usuario (UI), detecta la biblioteca activa del proyecto (sistema de componentes o motor de utilidades CSS nativo) y busca un componente existente. Esta disciplina es auditada y aplicada por [`./skills/design-system-auditor/SKILL.md`](./skills/design-system-auditor/SKILL.md).

- **Prioridad de Biblioteca Nativa (`Library-First`):** Si el proyecto utiliza una biblioteca de estilos o componentes instalada, todo lo actual y futuro estándar se construye con esa misma biblioteca. El catálogo `./specs/` solo entra a generar un componente nuevo desde cero cuando el usuario busca un componente **más abstracto, distinto o que la biblioteca no posea**.
- **Estandarización, Corrección y Optimización Activa en las Vistas:** Cuando el agente audita una vista existente (ej. con Playwright), su deber es **estandarizar, arreglar, optimizar y mejorar directamente el código de la vista** dentro de su biblioteca:
  1. **Corregir mal contraste (WCAG AA `< 4.5:1`)** entre botones, badges, chips y textos.
  2. **Unificar 2 clases distintas para 2 cajas iguales:** si dos elementos hermanos cumplen la misma función, deben usar exactamente las mismas clases de sombra, borde, padding y transición de la biblioteca, eliminando valores arbitrarios dispares.
  3. **Normalizar variables de tamaño de texto y fuentes:** eliminar la dispersión de tamaños y familias tipográficas entre elementos equivalentes.
  4. **Garantizar usabilidad táctil (`hitbox >= 44x44px`) y soporte `@media (prefers-reduced-motion: reduce)`.**

- **El problema:** Diseñar elementos desde cero usando etiquetas crudas (`<div>`, `<table>`, `<span>`) combinadas con clases de CSS/Tailwind es el error más frecuente. Esto produce un diseño inconsistente y un código base inflado de manera descontrolada.
- **La solución:** La reutilización mantiene la consistencia visual y de comportamiento. Los componentes del sistema de diseño ya contienen los tokens (colores, espaciados), densidades y patrones de interacción oficiales fijados en [`./DESIGN.md`](./DESIGN.md) o en el `DESIGN.md` de la raíz del proyecto.
- **Orden de prioridad para buscar componentes:**
  1. **Librería de Componentes Nucleares:** Revisa la carpeta principal de UI del proyecto (ej. `src/components/ui/`, `components/ui/`, `src/ui/`, `app/components/ui/`, `packages/ui/` o la biblioteca compartida del proyecto). En el 90% de los casos, detente aquí.
  2. **Componentes Locales o Compartidos Antiguos:** Revisa los directorios locales del módulo antes de asumir que algo no existe.
  3. **Propuestas de Extensión:** Si ningún componente se adapta perfectamente a lo que necesitas, indícalo explícitamente y propón extender un componente existente con una nueva propiedad antes de crear uno nuevo. No dupliques código en silencio. Consulta la matriz de decisiones en [`./skills/design-system-auditor/SKILL.md`](./skills/design-system-auditor/SKILL.md).
- **Catálogo de sustituciones comunes** (Asegúrate de mapear esto en el ecosistema actual):
  - ¿Vas a crear una tabla manual? → Usa el componente `Table` global (con paginación y ordenamiento nativo).
  - ¿Vas a crear un badge o contador? → Usa `Badge` o `Tag`.
  - ¿Vas a crear un menú desplegable? → Usa `Dropdown` o `Menu` junto con un disparador oficial.
  - ¿Vas a formatear fechas? → Usa el componente de internacionalización/fechas global del proyecto (ej. `<FormatDate />`), nunca manipules strings con librerías nativas directamente en el componente visual.
- **Evita el "Efecto IA" (Slop Visual):** Si construyes algo personalizado, usa estrictamente los tokens del sistema definidos en `DESIGN.md`. Está prohibido añadir degradados de colores genéricos, efectos de desenfoque de vidrio (glassmorphism), textos con gradientes, o animaciones decorativas innecesarias que degraden el rendimiento. Revisa la sección de Slop Visual en [`./skills/writing-ui-components/references/anti-patterns.md`](./skills/writing-ui-components/references/anti-patterns.md).

---

## Regla 2 — Ubicación correcta del código por Dominio/Módulo

La arquitectura debe estar segmentada por módulos o productos. Un directorio general de vistas o pantallas no es el vertedero predeterminado para cualquier UI.

- Antes de añadir un archivo a una carpeta global de escenas o vistas, verifica si pertenece a un submódulo específico o a un dominio de negocio independiente.
- Mantener la separación de dominios optimiza los tiempos de compilación, las pruebas automatizadas y los flujos de integración continua (CI/CD).

---

## Regla 3 — Prohibido escribir tipos de API a mano; usa Codegen

El backend (o el esquema de la API/Swagger/OpenAPI) es la única fuente de verdad.

- Nunca escribas un `interface` o un `type` en TypeScript que replique la respuesta de un endpoint del backend. Importa siempre los tipos generados automáticamente por las herramientas del proyecto.
- **No edites los archivos generados:** Los directorios con sufijos `*generated*` o esquemas automáticos nunca deben modificarse manualmente. Si la API cambia, se debe actualizar el backend o el esquema y volver a ejecutar el comando de generación de código (codegen).

---

## Regla 4 — Lógica de negocio fuera de los componentes visuales

- **Separación de responsabilidades:** Los componentes de React/Vue deben ser lo más puros y visuales posible.
- **Gestión de estado:** Toda la lógica pesada, llamadas a la API, filtrados de datos y efectos secundarios deben residir en la capa de gestión de estado correspondiente (ej. tiendas de Redux, Zustand, Kea, Pinia, o hooks contenedores dedicados), no incrustados directamente en el marcado del componente.

---

## Regla 5 — Estructura de archivos y abstracción limpia

Al crear, modificar, dividir o extraer componentes, aplica estrictamente las directrices de [`./skills/writing-ui-components/SKILL.md`](./skills/writing-ui-components/SKILL.md) y consulta [`./skills/writing-ui-components/references/anti-patterns.md`](./skills/writing-ui-components/references/anti-patterns.md).

- **Un componente por archivo:** El archivo debe llamarse igual que su exportación principal. Usa únicamente exportaciones nombradas (*named exports*). Evita los archivos índice comodín (`index.ts` tipo barril) para evitar dependencias circulares.
- **Regla de tres para componentes compartidos:** Extrae un componente compartido únicamente cuando el código en el que se invoca se lea como contenido y no como maquetación, y cuando ocurra en al menos tres lugares distintos (o dos lugares con una certeza absoluta de un tercero en camino). Si la abstracción requiere condicionales complejos para funcionar de manera distinta según quién lo llame, significa que no comparten la misma naturaleza: deja la duplicación local.
- **Interactividad nativa y accesible:** Los elementos que reciben clics deben ser semánticamente correctos. Usa etiquetas `<button>` o `<a>` (o sus equivalentes en el sistema de diseño). Nunca añadas eventos `onClick` sobre etiquetas `<div>`, `<span>` o tarjetas de contenedor.
- **Los tres estados obligatorios:** Las pantallas que cargan datos deben gestionar explícitamente tres escenarios visuales diferentes: Cargando (*Loading*), Vacío (*Empty*) y Error. Nunca deduzcas un estado "vacío" si los datos aún no han terminado de resolverse.
- **Congelamiento de identificadores públicos:** Al renombrar variables o símbolos de código, los strings expuestos (nombres de eventos analíticos, llaves de feature flags, atributos `data-*` de pruebas, rutas URL o llaves de `LocalStorage`) deben permanecer intactos. Son APIs públicas que rompen dashboards de analítica o pruebas de extremo a extremo (E2E).

---

## Regla 6 — Diseño responsivo enfocado en contenedores (No en pantallas)

Toda interfaz web debe soportar visualizaciones en espacios reducidos (por ejemplo, cuando el usuario abre un panel lateral de configuración o reduce el tamaño de su ventana de trabajo) y cumplir con las normas de accesibilidad de [`./skills/accessibility-contrast-auditor/SKILL.md`](./skills/accessibility-contrast-auditor/SKILL.md) y [`./DESIGN.md`](./DESIGN.md).

- **Usa Consultas de Contenedor (*Container Queries*), no de pantalla (*Viewport Queries*):** Los breakpoints tradicionales (`md:`, `lg:`) evalúan el ancho total de la ventana del navegador. Sin embargo, un componente dentro de un panel lateral puede tener un espacio real de apenas 400px en una pantalla gigante. Programa el comportamiento responsivo basándote en el espacio disponible de su contenedor.
- **Cero desbordamientos:** Nada debe cortarse de forma abrupta ni generar barras de desplazamiento horizontal inesperadas. Usa envolturas de flexbox (`flex-wrap`) para filas de botones o etiquetas, trunca cadenas de texto largas mediante elipses y apila columnas dobles verticalmente si el espacio se reduce.
- **Prioriza el contenido sobre la decoración:** Si el espacio es crítico, elimina ilustraciones, iconos secundarios o reduce márgenes de espaciado antes de sacrificar el texto explicativo o el botón de acción principal.
- **Hitboxes táctiles accesibles:** Cualquier elemento cliqueable debe contar con un área de interacción mínima de 44x44px según se estipula en [`./DESIGN.md`](./DESIGN.md) y [`./skills/accessibility-contrast-auditor/SKILL.md`](./skills/accessibility-contrast-auditor/SKILL.md).
- **No asumas un entorno móvil de forma errónea:** "Espacio estrecho" en aplicaciones web internas o SaaS no significa un teléfono móvil; significa un panel acoplado o una pantalla dividida en un monitor de escritorio. No agregues comportamientos táctiles a menos que el producto lo requiera explícitamente.

---

## Regla 7 — Protección contra fallos de extensiones de traducción (React-specific)

Las extensiones de traducción automática del navegador (como Google Translate) reemplazan los nodos de texto directo con elementos HTML propietarios (como `<font>`). Si React intenta actualizar un nodo de texto que ha sido reemplazado o tiene hermanos sueltos, la aplicación lanzará un error crítico de ejecución (`NotFoundError: Failed to execute 'removeChild' on 'Node'`).

- **El peligro:** Cadenas de texto combinadas con variables dinámicas de forma directa:

  ```tsx
  {/* MAL: Produce nodos de texto hermanos propensos a romperse */}
  <div>Resultado: {contador} ítems</div>
  ```

- **La solución:** Envuelve la sección dinámica o todo el conjunto en etiquetas estables independientes y, de ser necesario, bloquea la traducción en elementos puramente numéricos o de código mediante el atributo estándar `translate="no"`:

  ```tsx
  {/* BIEN: Nodos protegidos y aislados estructuralmente */}
  <span>Resultado: </span>
  <strong translate="no">{contador} ítems</strong>
  ```

---

## Cadencia de Verificación (Optimización de tiempo de ejecución)

Los linters y los chequeos de tipado estático son costosos en proyectos grandes. Sigue este orden de trabajo:

1. **Durante el desarrollo:** Confía exclusivamente en el servidor de lenguaje del editor (LSP) y en los errores en tiempo real en tu consola de desarrollo.
2. **Antes de finalizar la tarea:** Ejecuta el comando de verificación estática completo (ej. `npm run typecheck`, `pnpm lint:fix` o `python scripts/playwright_audit.py`) exactamente una vez antes de dar por terminado tu trabajo, evitando saturar los recursos en cada pequeño cambio.

---

## Regla 8 — Política Estricta Anti-Mock, Auto-Spec Discovery y Agnolicismo en `./specs/`

1. **Prohibido Inventar Datos o Vistas Artificiales:** El agente **NUNCA** debe fabricar métricas, textos o datos ficticios si el DOM origen no los tiene, ni generar páginas de demostración no solicitadas.
2. **Auto-Spec Discovery & Generation:** Si al auditar un sitio en cualquier framework (`Vue.js`, `Angular`, `React`, `Svelte`, `HTML`) con Playwright se descubre un componente abstracto que aún no posee su `.spec.md` en [`./specs/`](./specs/), el agente genera automáticamente el archivo `.spec.md` faltante (con las 3 secciones obligatorias: `🎯 Fingerprint & Heuristic Matching`, `📐 Component Interface & Props`, `♿ Reglas de Accesibilidad (a11y) & Estados`) y lo registra en [`./COMPONENTS.md`](./COMPONENTS.md).
3. **Zero-Vendor Branding en `./specs/`:** Mientras en las vistas del proyecto se prioriza y respeta la biblioteca instalada, las especificaciones dentro de `./specs/` y `./COMPONENTS.md` se mantienen 100% agnósticas y libres de nombres comerciales de terceros.
