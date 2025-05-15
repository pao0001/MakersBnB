DROP TABLE IF EXISTS properties;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    phone_number VARCHAR(20) NOT NULL,
    password_hash VARCHAR(100) NOT NULL
);

CREATE TABLE properties (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    phone_number VARCHAR(20) NOT NULL,
    address VARCHAR(255) NOT NULL,
    description VARCHAR(255) NOT NULL,
    price_per_night DECIMAL(10, 2) NOT NULL,
    availability VARCHAR(255) NOT NULL,
    user_id INT NOT NULL --REFERENCES users(id)
);

-- Insert sample data into users table
INSERT INTO users (name, email, phone_number, password_hash) VALUES
  ('John Doe', 'johndoe@bing.com' , '1234567890', '$2b$12$BI104770ilO1DyhxM.1zQeBiKWVFKkUO3K/QBCUBFD//ZqU.cEZhu'), -- password123
  ('Alice Smith', 'alice@example.com', '0987654321', '$2b$12$hYzSsmkkHJkUJtogiBG3Sut7Nbm3GQDaI5dOCzTfGAlyZwOhg4N1G'), -- letmein!
  ('Bob Johnson', 'bob.j@staymail.com', '07700900000', '$2b$12$fQ3g8iCtqdKNYfgqOaQCWe.FRLF3V3UPMvxxD.ZTBhJo4QhENW46q'); -- securepass

INSERT INTO properties (name, email, phone_number, address, description, price_per_night, availability, user_id) VALUES
  ('John Doe', 'johndoe@bing.com' , '1234567890', '123 Main St, Cityville', 'A lovely place to stay.', 100.00, 'available', 1),
  ('Alice Smith', 'alice@example.com', '0987654321', '45 River Road, Lakeside', 'Peaceful lake house with mountain views.', 150.00, 'available', 2),
  ('Bob Johnson', 'bob.j@staymail.com', '07700900000', '9 Hilltop Avenue, Countryside', 'Charming countryside cottage with garden.', 85.00, 'unavailable', 3);
