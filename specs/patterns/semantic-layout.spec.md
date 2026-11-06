# SPEC: Semantic Layout & Page Blueprint Normalization

## Matriz de Ordenamiento Semántico Global
| Tag HTML5 | Rol Layout | Componentes Permitidos | Reglas de Jerarquía |
| :--- | :--- | :--- | :--- |
| `<header>` | Cabecera Global | Logo, Nav, Search, UserProfile | Exactamente 1 por página/módulo superior |
| `<nav>` | Navegación | Tabs, Breadcrumbs, Links | Debe ir dentro de `<header>`, `<aside>` o `<main>` |
| `<main>` | Área Principal | Sections, Grids, Dashboards | Único en el documento |
| `<section>` | Bloque Temático | KPI Grid, Chart Card, Data Table | Debe contener una etiqueta de encabezado (`h2-h6`) |
| `<aside>` | Panel Lateral | Slicers, Filters, Sidebar Nav | Independiente o flotante |
| `<footer>` | Pie de Página | Credits, Version, Copyright | Ubicado al final del flujo |