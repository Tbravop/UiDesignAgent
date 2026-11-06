# Skill Spec: UI Library Spec Extractor & On-The-Fly Spec Generator

Skill agnóstica para auditar y extraer especificaciones `.spec.md` tanto desde documentaciones de referencia como **en caliente durante la auditoría de cualquier proyecto (`Vue.js`, `Angular`, `React`, `Svelte`, `HTML`)** cuando Playwright detecta un componente que aún no existe en `./specs/`.

---

## 1. Disparadores de Ejecución
1. **Durante `/design-system-auditor` (Auto-Spec Discovery):** Cuando `./Skills/playwright-inspector.md` detecta un componente o patrón en la página auditada que no tiene `.spec.md` en `./specs/`.
2. **Al estudiar un catálogo o librería externa:** Para ampliar el vocabulario base de `./specs/` traduciendo patrones a contratos agnósticos.

## 2. Protocolo de Generación del Archivo `.spec.md`
1. **Clasificación Atómica:**
   - **Átomo (`./specs/atoms/{nombre}.spec.md`):** Elemento indivisible (ej. `avatar`, `separator`, `button`, `badge`, `chip`, `spinner`).
   - **Molécula (`./specs/molecules/{nombre}.spec.md`):** Agrupación funcional de 2 a 4 átomos (ej. `card`, `hover-card`, `context-menu`, `input-group`, `button-group`).
   - **Organismo (`./specs/organisms/{nombre}.spec.md`):** Sección autónoma compleja (ej. `navbar`, `command-palette`, `modal`, `offcanvas`, `data-table-slicer`).
2. **Estructura Obligatoria de 3 Secciones:**
   - `## 1. 🎯 Fingerprint & Heuristic Matching` (Selectores semánticos, roles ARIA y heurística de caja en Playwright).
   - `## 2. 📐 Component Interface & Props` (Interfaz en TypeScript 100% agnóstica y mapeo a tokens OKLCH y `clamp()` de `./DESIGN.md`).
   - `## 3. ♿ Reglas de Accesibilidad (a11y) & Estados` (Teclado, foco visible, hitboxes `>= 44px` y `prefers-reduced-motion`).
3. **Regla Zero-Vendor Branding:**
   - Eliminar cualquier nombre comercial de framework o librería externa y cualquier clase CSS propietaria.
4. **Actualización del Catálogo:**
   - Registrar inmediatamente la nueva spec en `./COMPONENTS.md` usando ruta relativa POSIX (`./specs/...`).
