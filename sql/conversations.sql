-- Drop the existing policy (destructive)
DROP POLICY "Users can view and update their own conversations." ON public.conversations;

-- Ensure RLS is enabled (no-op if already enabled)
ALTER TABLE public.conversations ENABLE ROW LEVEL SECURITY;

-- Index to speed policy checks
CREATE INDEX IF NOT EXISTS idx_conversations_user_id ON public.conversations(user_id);

-- Create explicit, per-operation policies using SELECT auth.uid() pattern
CREATE POLICY "Conversations: select by owner" ON public.conversations
  FOR SELECT
  TO authenticated
  USING ((SELECT auth.uid()) = user_id);

CREATE POLICY "Conversations: insert by owner" ON public.conversations
  FOR INSERT
  TO authenticated
  WITH CHECK ((SELECT auth.uid()) = user_id);

CREATE POLICY "Conversations: update by owner" ON public.conversations
  FOR UPDATE
  TO authenticated
  USING ((SELECT auth.uid()) = user_id)
  WITH CHECK ((SELECT auth.uid()) = user_id);

CREATE POLICY "Conversations: delete by owner" ON public.conversations
  FOR DELETE
  TO authenticated
  USING ((SELECT auth.uid()) = user_id);
