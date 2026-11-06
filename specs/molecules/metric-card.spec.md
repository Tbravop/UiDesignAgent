# SPEC: MoleculeMetricCard (Metric Card & Data Morphing Contract)

## 1. Component Interface
```typescript
export interface MetricDataPoint {
  id: string;
  label: string;
  value: number;
}

export interface MetricCardProps {
  title: string;
  currentValue: string | number;
  trendPercentage: number;
  activeFilterKey: string;
  dataSeries: MetricDataPoint[];
  onFilterChange: (filterKey: string) => void;
}
```

## 2. Motion & Transition Rules
- **Value Morphing:** Fade & translate Y en cambios de filtro (`--duration-sm` / 200ms).
- **SVG Morphing:** Interpolación de barras SVG (`transition: y, height` en 400ms con `--ease-in-out-cubic`).
- **Reduced Motion:** Desactivación instantánea bajo `@media (prefers-reduced-motion: reduce)`.