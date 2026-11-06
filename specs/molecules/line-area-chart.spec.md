# SPEC: MoleculeLineAreaChart (Line, Area, Ribbon & Waterfall Charts)

```typescript
export type TrendChartType = 'line' | 'area' | 'stacked-area' | 'line-clustered-column' | 'line-stacked-column' | 'ribbon' | 'waterfall';

export interface DataPoint {
  x: string | number;
  y: number;
}

export interface TrendChartProps {
  type: TrendChartType;
  series: { id: string; label: string; points: DataPoint[]; }[];
}
```