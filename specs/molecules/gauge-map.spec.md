# SPEC: MoleculeGaugeMap (Gauge & Local Shape Maps)

```typescript
export interface GaugeChartProps {
  currentValue: number;
  targetValue: number;
}

export interface ShapeMapProps {
  topoJsonUrl?: string;
  regionData: Record<string, number>;
}
```