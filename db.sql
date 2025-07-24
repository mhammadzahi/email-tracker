CREATE TABLE email_tracking (
    id SERIAL PRIMARY KEY,
    email_id VARCHAR(255) NOT NULL,
    ip_address INET NOT NULL,
    user_agent TEXT,
    timestamp TIMESTAMPTZ NOT NULL,
);
