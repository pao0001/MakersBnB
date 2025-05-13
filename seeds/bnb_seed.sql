DROP TABLE IF EXISTS properties;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    password_hash VARCHAR(255) NOT NULL
);

CREATE TABLE properties (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    address VARCHAR(255) NOT NULL,
    description VARCHAR(255) NOT NULL,
    price_per_night DECIMAL(10, 2) NOT NULL,
    availability VARCHAR(255) NOT NULL,
    user_id INT NOT NULL REFERENCES users(id)
);

-- Insert sample data into users table
INSERT INTO users (name, email, phone, password_hash) VALUES
('John Doe', 'johndoe@bing.com' , '1234567890', 'hashed_password_1');

INSERT INTO properties (name, email, phone, address, description, price_per_night, availability, user_id) VALUES
('John Doe', 'johndoe@bing.com' , '1234567890', '123 Main St, Cityville', 'A lovely place to stay.', 100.00, 'available', 1);