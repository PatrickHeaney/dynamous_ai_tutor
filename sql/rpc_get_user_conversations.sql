CREATE OR REPLACE FUNCTION get_user_conversations()
RETURNS SETOF conversations
LANGUAGE plpgsql
SECURITY DEFINER -- This allows the function to run with the privileges of the function owner (typically postgres), but we'll still filter by auth.uid()
AS $$
BEGIN
  RETURN QUERY
  SELECT *
  FROM conversations
  WHERE user_id = auth.uid();
END;
$$;

-- Grant execution privileges to authenticated users
GRANT EXECUTE ON FUNCTION get_user_conversations() TO authenticated;
