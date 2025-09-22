CREATE TABLE IF NOT EXISTS user_profiles (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT now(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT now(),
    external_id TEXT UNIQUE, -- e.g., email, username from an auth system
    name TEXT,
    preferences JSONB DEFAULT '{}'::jsonb -- e.g., learning style, topics of interest
);

-- Enable Row Level Security (RLS)
ALTER TABLE user_profiles ENABLE ROW LEVEL SECURITY;

-- Policy for users to view and update their own profile
CREATE POLICY "Users can view and update their own profile."
ON user_profiles FOR ALL
USING (auth.uid() = id)
WITH CHECK (auth.uid() = id);

-- Policy for users to insert their own profile (if external_id is used for initial creation)
CREATE POLICY "Users can insert their own profile."
ON user_profiles FOR INSERT
WITH CHECK (auth.uid() IS NOT NULL); -- Adjust if you have specific external_id logic for RLS
