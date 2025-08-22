export interface Item {
  id: number;
  sku: string;
  name: string;
  description?: string | null;
  min_qty: number;
  is_active: boolean;
}

export interface Location {
  id: number;
  code: string;
  name: string;
}
