# SPEC: MoleculeProportionChart (Scatter, Funnel, Treemap, Pie & Donut Charts)

```typescript
export type ProportionChartType = 'scatter' | 'funnel' | 'treemap' | 'pie' | 'donut';

export interface SliceData {
  id: string;
  label: string;
  value: number;
  colorToken: string;
}

export interface ProportionChartProps {
  type: ProportionChartType;
  data: SliceData[];
  centerLabel?: string;
  centerValue?: string;
}
```