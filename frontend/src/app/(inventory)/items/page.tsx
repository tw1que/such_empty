import DataTable from '@/components/DataTable';
import ItemForm from '@/components/ItemForm';
import { get, post } from '@/lib/api';
import type { Item } from '@/types';

export default async function ItemsPage() {
  const items = await get<Item[]>('/api/v1/items');
  return (
    <div>
      <h1>Items</h1>
      <ItemForm onSubmit={async (data) => { await post('/api/v1/items', data); }} />
      <DataTable
        columns={[
          { key: 'id', label: 'ID' },
          { key: 'sku', label: 'SKU' },
          { key: 'name', label: 'Name' },
        ]}
        data={items}
      />
    </div>
  );
}
