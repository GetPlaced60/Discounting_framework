CREATE DATABASE discount_db;
USE discount_db;

CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    price DECIMAL(10, 2),
    discount_rate DECIMAL(5, 2)
);
