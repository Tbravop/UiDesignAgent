# Skill Spec: Library-First Standardizer & Abstract Component Builder

Skill encargada de decidir cuándo estandarizar/optimizar directamente en las vistas usando la biblioteca nativa del proyecto y cuándo construir un componente abstracto en `./src/components/` guiado por `./specs/`.

---

## 1. Regla de Prioridad: Biblioteca Nativa Primero (`Library-First`)
1. Si el repositorio utiliza una biblioteca de estilos o componentes nativa:
   - **Todo componente estándar actual o futuro se construye con la biblioteca del proyecto.**
   - **No** se crean hojas de estilo paralelas que dupliquen lo que la biblioteca ya provee.
2. **Estandarización Activa sobre las Vistas Existentes:**
   - El agente inspecciona las vistas (`index.html`, `.vue`, `.tsx`, `.component.html`) y **corrige in-place**:
     - **Mal contraste (`< 4.5:1` WCAG AA)** en botones, badges y chips.
     - **2 clases distintas para 2 cajas iguales:** unifica sombras, bordes, desplazamientos y paddings en elementos hermanos para que usen exactamente la misma estructura de clases de la biblioteca.
     - **Variables de tamaño de texto y fuentes dispersas:** normaliza las familias tipográficas (`font-label-mono`, `font-display`, `font-body-md`) y la escala de tamaños por jerarquía.
     - **Usabilidad y Accesibilidad:** garantiza hitboxes mínimos de `44x44px` (`min-h-[44px]`) y añade `@media (prefers-reduced-motion: reduce)`.

## 2. Cuándo Construir en `./src/components/` con `./specs/`
- Únicamente cuando el usuario solicita un **componente más abstracto, distinto o compuesto** que la biblioteca nativa no resuelve de fábrica, o cuando en un proyecto con framework (`Vue`, `Angular`, `React`, `Svelte`) se requiere encapsular dicho componente abstracto siguiendo el contrato de `./specs/`.
