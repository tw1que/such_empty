import type { ReactNode } from 'react';

interface Column<T> {
  key: keyof T;
  label: string;
}
interface Props<T> {
  columns: Column<T>[];
  data: T[];
}

export default function DataTable<T extends Record<string, unknown>>({
  columns,
  data,
}: Props<T>) {
  return (
    <table>
      <thead>
        <tr>
          {columns.map((c) => (
            <th key={String(c.key)}>{c.label}</th>
          ))}
        </tr>
      </thead>
      <tbody>
        {data.map((row, i) => (
          <tr key={i}>
            {columns.map((c) => (
              <td key={String(c.key)}>{String(row[c.key])}</td>
            ))}
          </tr>
        ))}
      </tbody>
    </table>
  );
}
