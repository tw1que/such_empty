'use client';

import { zodResolver } from '@hookform/resolvers/zod';
import { useForm } from 'react-hook-form';
import { z } from 'zod';

const schema = z.object({
  sku: z.string(),
  name: z.string(),
  description: z.string().optional(),
  min_qty: z.number().int().default(0),
  is_active: z.boolean().default(true),
});

type ItemFormValues = z.infer<typeof schema>;

export default function ItemForm({
  onSubmit,
  initial,
}: {
  onSubmit: (values: ItemFormValues) => void;
  initial?: Partial<ItemFormValues>;
}) {
  const { register, handleSubmit } = useForm<ItemFormValues>({
    resolver: zodResolver(schema),
    defaultValues: initial,
  });

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <input {...register('sku')} placeholder="SKU" />
      <input {...register('name')} placeholder="Name" />
      <textarea {...register('description')} placeholder="Description" />
      <input type="number" {...register('min_qty', { valueAsNumber: true })} />
      <label>
        <input type="checkbox" {...register('is_active')} /> Active
      </label>
      <button type="submit">Save</button>
    </form>
  );
}
