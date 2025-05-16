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

-- Users (20 entries)
INSERT INTO users (name, email, phone_number, password_hash) VALUES
  ('John Doe', 'johndoe@bing.com' , '1234567890', '$2b$12$BI104770ilO1DyhxM.1zQeBiKWVFKkUO3K/QBCUBFD//ZqU.cEZhu'), -- password123
  ('Alice Smith', 'alice@example.com', '0987654321', '$2b$12$hYzSsmkkHJkUJtogiBG3Sut7Nbm3GQDaI5dOCzTfGAlyZwOhg4N1G'), -- letmein!
  ('Bob Johnson', 'bob.j@staymail.com', '07700900000', '$2b$12$fQ3g8iCtqdKNYfgqOaQCWe.FRLF3V3UPMvxxD.ZTBhJo4QhENW46q'), -- securepass
  ('Eve Carter', 'eve.carter@mail.com', '07123456789', 'password_hash_placeholder'),
  ('Frank Lee', 'frank.lee@example.com', '07234567890', 'password_hash_placeholder'),
  ('Grace Kim', 'grace.kim@mail.com', '07345678901', 'password_hash_placeholder'),
  ('Henry Adams', 'henry.adams@domain.com', '07456789012', 'password_hash_placeholder'),
  ('Ivy Clark', 'ivy.clark@mail.com', '07567890123', 'password_hash_placeholder'),
  ('Jack Wright', 'jack.wright@example.com', '07678901234', 'password_hash_placeholder'),
  ('Karen Young', 'karen.young@mail.com', '07789012345', 'password_hash_placeholder'),
  ('Leo Martin', 'leo.martin@domain.com', '07890123456', 'password_hash_placeholder'),
  ('Mia Turner', 'mia.turner@mail.com', '07901234567', 'password_hash_placeholder'),
  ('Noah Scott', 'noah.scott@example.com', '07012345678', 'password_hash_placeholder'),
  ('Olivia Evans', 'olivia.evans@mail.com', '07123456780', 'password_hash_placeholder'),
  ('Paul Green', 'paul.green@domain.com', '07234567801', 'password_hash_placeholder'),
  ('Quinn Hall', 'quinn.hall@mail.com', '07345678012', 'password_hash_placeholder'),
  ('Rachel Baker', 'rachel.baker@example.com', '07456780123', 'password_hash_placeholder'),
  ('Steve Young', 'steve.young@mail.com', '07567801234', 'password_hash_placeholder'),
  ('Tina King', 'tina.king@domain.com', '07678012345', 'password_hash_placeholder'),
  ('Uma Collins', 'uma.collins@mail.com', '07780123456', 'password_hash_placeholder');

-- Properties (20 entries)
INSERT INTO properties (name, email, phone_number, address, description, price_per_night, availability, user_id) VALUES
  ('John Doe', 'johndoe@bing.com' , '1234567890', '123 Main St, Cityville', 'A lovely place to stay.', 100.00, 'available', 1),
  ('Alice Smith', 'alice@example.com', '0987654321', '45 River Road, Lakeside', 'Peaceful lake house with mountain views.', 150.00, 'available', 2),
  ('Bob Johnson', 'bob.j@staymail.com', '07700900000', '9 Hilltop Avenue, Countryside', 'Charming countryside cottage with garden.', 85.00, 'unavailable', 3),
  ('Eve Carter', 'eve.carter@mail.com', '07123456789', '101 Oak Street, Midtown', 'Modern apartment close to downtown.', 120.00, 'available', 4),
  ('Frank Lee', 'frank.lee@example.com', '07234567890', '202 Pine Lane, Suburbia', 'Cozy suburban home with backyard.', 90.00, 'available', 5),
  ('Grace Kim', 'grace.kim@mail.com', '07345678901', '303 Birch Blvd, Riverside', 'Riverside cabin with great views.', 130.00, 'unavailable', 6),
  ('Henry Adams', 'henry.adams@domain.com', '07456789012', '404 Cedar Court, Hillside', 'Spacious villa on a hill.', 200.00, 'available', 7),
  ('Ivy Clark', 'ivy.clark@mail.com', '07567890123', '505 Elm Street, Downtown', 'Stylish loft in city center.', 140.00, 'available', 8),
  ('Jack Wright', 'jack.wright@example.com', '07678901234', '606 Spruce Drive, Seaside', 'Beachfront property with ocean views.', 220.00, 'unavailable', 9),
  ('Karen Young', 'karen.young@mail.com', '07789012345', '707 Maple Avenue, Oldtown', 'Historic home with modern amenities.', 110.00, 'available', 10),
  ('Leo Martin', 'leo.martin@domain.com', '07890123456', '808 Walnut Street, Uptown', 'Elegant townhouse near park.', 125.00, 'available', 11),
  ('Mia Turner', 'mia.turner@mail.com', '07901234567', '909 Chestnut Blvd, Midtown', 'Contemporary apartment with gym access.', 135.00, 'available', 12),
  ('Noah Scott', 'noah.scott@example.com', '07012345678', '1001 Aspen Way, Countryside', 'Quiet retreat surrounded by nature.', 95.00, 'unavailable', 13),
  ('Olivia Evans', 'olivia.evans@mail.com', '07123456780', '1102 Willow Road, Lakeside', 'Cozy cottage near the lake.', 105.00, 'available', 14),
  ('Paul Green', 'paul.green@domain.com', '07234567801', '1203 Poplar Street, Suburbia', 'Family home with large garden.', 115.00, 'available', 15),
  ('Quinn Hall', 'quinn.hall@mail.com', '07345678012', '1304 Fir Lane, Hillside', 'Charming bungalow with views.', 125.00, 'unavailable', 16),
  ('Rachel Baker', 'rachel.baker@example.com', '07456780123', '1405 Pine Street, Downtown', 'Modern condo with balcony.', 130.00, 'available', 17),
  ('Steve Young', 'steve.young@mail.com', '07567801234', '1506 Cedar Drive, Uptown', 'Luxury apartment near nightlife.', 180.00, 'available', 18),
  ('Tina King', 'tina.king@domain.com', '07678012345', '1607 Birch Avenue, Oldtown', 'Classic home with fireplace.', 115.00, 'available', 19),
  ('Uma Collins', 'uma.collins@mail.com', '07780123456', '1708 Oak Court, Riverside', 'Cozy riverside cabin.', 125.00, 'unavailable', 20);
