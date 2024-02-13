CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    amount INT,
    currency VARCHAR(10),
    status VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
