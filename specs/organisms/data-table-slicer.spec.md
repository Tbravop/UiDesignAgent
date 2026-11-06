# SPEC: OrganismDataTableSlicer (Cards, Multi-row Cards, Tables, Matrices & Slicers)

```typescript
export interface ColumnDef<T> {
  header: string;
  accessorKey: keyof T;
}

export interface TableProps<T> {
  data: T[];
  columns: ColumnDef<T>[];
  isHierarchical?: boolean;
}
```