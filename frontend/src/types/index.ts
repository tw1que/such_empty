export interface Item extends Record<string, unknown> {
  id: number;
  sku: string;
  name: string;
  description?: string | null;
  min_qty: number;
  is_active: boolean;
}

export interface Location extends Record<string, unknown> {
  id: number;
  code: string;
  name: string;
}
