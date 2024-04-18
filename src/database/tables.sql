CREATE TABLE meters (
  id INT PRIMARY KEY AUTO_INCREMENT,  -- Auto-incrementing integer for unique ID
  meter_number VARCHAR(20) NOT NULL UNIQUE, -- Meter number (unique identifier)
  owner VARCHAR(255) NOT NULL,               -- Owner of the meter
  location VARCHAR(255) NOT NULL,             -- Location of the meter
  current_balance DECIMAL(10,2) NOT NULL DEFAULT 0.0 -- Current balance (with decimals for precision)
);

CREATE TABLE tokens (
  id INT PRIMARY KEY AUTO_INCREMENT,  -- Auto-incrementing integer for unique ID
  meter_number VARCHAR(250),                    -- Foreign key referencing the meters table
  amount DECIMAL(10,2) NOT NULL,        -- Value associated with the token (amount in currency)
  token_code VARCHAR(20) UNIQUE NOT NULL,     -- Unique token identifier (generated string)
  created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP, -- Timestamp of token creation
  electricity_units DECIMAL(10,2) NOT NULL DEFAULT 0.0,  -- Electricity units associated with the token
);