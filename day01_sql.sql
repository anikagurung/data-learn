-- Day 1: SQL Basics

-- ============================================================
-- 1. CREATE TABLE
-- ============================================================

CREATE TABLE cars (
    brand VARCHAR(255),
    model VARCHAR(255),
    year INT
);

-- Insert a record
INSERT INTO cars (brand, model, year)
VALUES ('Ford', 'Mustang', 1964);

-- View all records
SELECT * FROM cars;

-- Select specific columns
SELECT brand, year
FROM cars;


-- ============================================================
-- 2. ALTER TABLE - ADD COLUMN
-- ============================================================

ALTER TABLE cars
ADD color VARCHAR(255);

-- Update a record
UPDATE cars
SET color = 'red'
WHERE brand = 'Ford';

SELECT * FROM cars;


-- ============================================================
-- 3. DROP COLUMN
-- ============================================================

ALTER TABLE cars
DROP COLUMN color;


-- ============================================================
-- 4. DELETE
-- ============================================================

DELETE FROM cars
WHERE brand = 'Volvo';


-- ============================================================
-- 5. ALTER COLUMN DATA TYPE
-- ============================================================

ALTER TABLE cars
ALTER COLUMN year TYPE VARCHAR(4);

SELECT * FROM cars;


-- ============================================================
-- 6. SELECT AND DISTINCT
-- ============================================================

-- Example using the customers table from the practice material
SELECT customer_name, country
FROM customers;

SELECT DISTINCT country
FROM customers;

SELECT COUNT(DISTINCT country)
FROM customers;


-- ============================================================
-- 7. WHERE
-- ============================================================

SELECT *
FROM customers
WHERE city = 'London';


-- ============================================================
-- 8. ORDER BY
-- ============================================================

SELECT *
FROM products
ORDER BY price;

SELECT *
FROM products
ORDER BY price DESC;


-- ============================================================
-- 9. LIMIT
-- ============================================================

SELECT *
FROM customers
LIMIT 20;


-- ============================================================
-- 10. OFFSET
-- ============================================================

SELECT *
FROM customers
LIMIT 20 OFFSET 40;


-- ============================================================
-- 11. MIN
-- ============================================================

SELECT MIN(price)
FROM products;

SELECT MIN(price) AS lowest_price
FROM products;


-- ============================================================
-- 12. MAX
-- ============================================================

SELECT MAX(price)
FROM products;


-- ============================================================
-- 13. COUNT
-- ============================================================

SELECT COUNT(customer_id)
FROM customers;

SELECT COUNT(customer_id)
FROM customers
WHERE city = 'London';


-- ============================================================
-- 14. SUM
-- ============================================================

SELECT SUM(quantity)
FROM order_details;


-- ============================================================
-- 15. AVG
-- ============================================================

SELECT AVG(price)
FROM products;

SELECT AVG(price)::NUMERIC(10,2)
FROM products;
