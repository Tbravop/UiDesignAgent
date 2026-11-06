# SPEC: MoleculeBarColumnChart (Bar & Column Charts)

```typescript
export type BarChartType = 'stacked-bar' | 'stacked-column' | 'clustered-bar' | 'clustered-column' | '100-stacked-bar' | '100-stacked-column';

export interface ChartSeries {
  id: string;
  label: string;
  colorToken: string;
  values: number[];
}

export interface BarColumnChartProps {
  type: BarChartType;
  categories: string[];
  series: ChartSeries[];
  showLegend?: boolean;
}
```