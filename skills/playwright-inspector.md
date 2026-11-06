# Skill Spec: Playwright Live DOM Inspector & Unmatched Cluster Detector

Skill para ejecutar el motor de Playwright activo en la Fase 0, Fase 1 y durante invocaciones de `/design-system-auditor` para escaneo en vivo de proyectos en cualquier framework (`Vue.js`, `Angular`, `React`, `Svelte`, `HTML`).

---

## 1. Auto-Instalación e Inicialización del Runtime
Antes de iniciar cualquier auditoría:
1. Comprobar `python -c "import playwright"`.
2. Si no está disponible, instalar de forma desatendida:
   ```powershell
   python -m pip install playwright
   python -m playwright install chromium
   ```

## 2. Extracción Topológica Computada
En un viewport de escritorio (`1440x900`) y móvil (`390x844`):
- Evaluar cada nodo semántico y control interactivo con `window.getComputedStyle(el)` y `el.getBoundingClientRect()`.
- Detectar polimorfismo funcional: enlaces `<a>` con `height >= 44px`, borde o sombra y padding simétrico se clasifican como `atom-button` (`as="a"`).
- Detectar layouts compuestos independientemente del sistema de clases: contenedores con 2 hijos directos en fila (`row`) y proporción `25%-45%` / `55%-75%` se clasifican como `molecule-card` (`orientation="horizontal"`).

## 3. Detección de Patrones sin Spec (`Unmatched DOM Clusters`)
Cuando el inspector detecta en el DOM un elemento interactivo o un clúster repetido (3 o más instancias o sección funcional diferenciada) cuya firma geométrica/ARIA no coincide con ningún archivo en `./specs/`:
1. Emite una alerta de **Missing Spec Detected** indicando:
   - Tag semántico, roles ARIA, dimensiones de caja y estructura de hijos.
   - Clasificación sugerida (`atoms`, `molecules` u `organisms`).
2. Dispara automáticamente la skill `./Skills/ui-library-spec-extractor.md` para generar el archivo `.spec.md` faltante antes de invocar a `./Skills/src-builder.md`.
