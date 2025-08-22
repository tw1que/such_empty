'use client';

import { zodResolver } from '@hookform/resolvers/zod';
import { useForm } from 'react-hook-form';
import { z } from 'zod';

const schema = z.object({
  code: z.string(),
  name: z.string(),
});

type LocationFormValues = z.infer<typeof schema>;

export default function LocationForm({
  onSubmit,
  initial,
}: {
  onSubmit: (values: LocationFormValues) => void;
  initial?: Partial<LocationFormValues>;
}) {
  const { register, handleSubmit } = useForm<LocationFormValues>({
    resolver: zodResolver(schema),
    defaultValues: initial,
  });
  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <input {...register('code')} placeholder="Code" />
      <input {...register('name')} placeholder="Name" />
      <button type="submit">Save</button>
    </form>
  );
}
