import DataTable from '@/components/DataTable';
import LocationForm from '@/components/LocationForm';
import { get, post } from '@/lib/api';
import type { Location } from '@/types';

export default async function LocationsPage() {
  const locations = await get<Location[]>('/api/v1/locations');
  return (
    <div>
      <h1>Locations</h1>
      <LocationForm onSubmit={async (data) => { await post('/api/v1/locations', data); }} />
      <DataTable
        columns={[
          { key: 'id', label: 'ID' },
          { key: 'code', label: 'Code' },
          { key: 'name', label: 'Name' },
        ]}
        data={locations}
      />
    </div>
  );
}
