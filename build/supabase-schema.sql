-- Progress tracking for the website (site/progress.html).
-- Run once in the Supabase dashboard: SQL Editor -> New query -> paste -> Run.
-- Each row is one mark: a knowledge point id (e.g. math/discrete/counting/derangements)
-- or a problem id (e.g. prob-counting-03) with its state.

create table if not exists public.progress (
  user_id    uuid        not null default auth.uid() references auth.users (id) on delete cascade,
  item       text        not null,
  state      text        not null check (state in ('new', 'learned', 'reviewing', 'mastered')),
  updated_at timestamptz not null default now(),
  primary key (user_id, item)
);

-- Row-level security: a signed-in user can only see and change their own rows.
-- Visitors who are not signed in can read and write nothing.
alter table public.progress enable row level security;

create policy "own rows: select" on public.progress
  for select to authenticated using (auth.uid() = user_id);
create policy "own rows: insert" on public.progress
  for insert to authenticated with check (auth.uid() = user_id);
create policy "own rows: update" on public.progress
  for update to authenticated using (auth.uid() = user_id) with check (auth.uid() = user_id);
create policy "own rows: delete" on public.progress
  for delete to authenticated using (auth.uid() = user_id);
