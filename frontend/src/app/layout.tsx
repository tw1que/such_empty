import Link from 'next/link';
import type { ReactNode } from 'react';

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="en">
      <body>
        <nav style={{ marginBottom: '1rem' }}>
          <Link href="/">Dashboard</Link> | <Link href="/items">Items</Link> |{' '}
          <Link href="/locations">Locations</Link>
        </nav>
        {children}
      </body>
    </html>
  );
}
