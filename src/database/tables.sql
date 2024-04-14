create table meters
(
    meter_id VARCHAR(50) PRIMARY KEY,
    nickname VARCHAR(100),
    tokens TEXT
);

CREATE TABLE tokens (
    id SERIAL PRIMARY KEY,
    token VARCHAR(50) NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    meter_id VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (meter_id) REFERENCES meters(meter_id)
);