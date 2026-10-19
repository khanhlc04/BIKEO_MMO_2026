-- Sổ Lãi 60 Ngày — schema Supabase, phiên bản KHÔNG đăng nhập.
-- Chạy 1 lần: Supabase Dashboard → SQL Editor → New query → dán toàn bộ → Run.
-- LƯU Ý: ai có link web (và anon key công khai trong web) đều đọc/ghi/xóa được. Giữ link kín, tải CSV định kỳ.

create table if not exists public.settings (
  id text primary key,
  brand text not null default '',
  capital bigint not null default 10000000,
  target bigint not null default 30000000,
  start_date date not null default '2026-11-03',
  end_date date not null default '2027-01-02',
  tax_pct numeric not null default 0,
  channels jsonb not null default '[]'::jsonb,
  products jsonb not null default '[]'::jsonb,
  updated_at timestamptz not null default now()
);

create table if not exists public.orders (
  id uuid primary key default gen_random_uuid(),
  order_date date not null,
  channel text not null,
  product text not null,
  qty int not null default 1 check (qty > 0),
  revenue bigint not null default 0,
  cogs bigint not null default 0,
  fee_pct numeric not null default 0,
  ship bigint not null default 0,
  status text not null default 'Đang giao' check (status in ('Đang giao','Đã giao','Hoàn','Hủy')),
  note text not null default '',
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);
create index if not exists orders_date_idx on public.orders(order_date);

create table if not exists public.expenses (
  id uuid primary key default gen_random_uuid(),
  expense_date date not null,
  category text not null,
  amount bigint not null default 0,
  note text not null default '',
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);
create index if not exists expenses_date_idx on public.expenses(expense_date);

-- RLS bật (bắt buộc với schema public) nhưng mở cho anon vì web không có đăng nhập
alter table public.settings enable row level security;
alter table public.orders   enable row level security;
alter table public.expenses enable row level security;

drop policy if exists "settings open" on public.settings;
create policy "settings open" on public.settings for all to anon, authenticated using (true) with check (true);
drop policy if exists "orders open" on public.orders;
create policy "orders open" on public.orders for all to anon, authenticated using (true) with check (true);
drop policy if exists "expenses open" on public.expenses;
create policy "expenses open" on public.expenses for all to anon, authenticated using (true) with check (true);

grant usage on schema public to anon, authenticated;
grant select, insert, update, delete on public.settings, public.orders, public.expenses to anon, authenticated;

-- Cài đặt ban đầu (vốn 10 triệu, mục tiêu 30 triệu, 3/11/2026 → 2/1/2027, phí sàn Q4/2026, 4 SKU)
insert into public.settings (id, brand, capital, target, start_date, end_date, tax_pct, channels, products) values (
  'main', 'Samesies', 10000000, 30000000, '2026-11-03', '2027-01-02', 0,
  '[{"name":"TikTok Shop","feePct":23.3},{"name":"Shopee","feePct":25.5},{"name":"Zalo / Instagram / Facebook","feePct":0},{"name":"Khác","feePct":0}]'::jsonb,
  '[{"name":"Áo nỉ Samesies (set 2 áo)","cost":212000,"price":499000},{"name":"Áo thun Samesies (set 2 áo)","cost":156000,"price":349000},{"name":"Vòng Samesies (cặp + hộp)","cost":45000,"price":149000},{"name":"Hộp Quà Kỷ Niệm Samesies (áo nỉ + vòng + hộp)","cost":265000,"price":599000}]'::jsonb
) on conflict (id) do nothing;
