-- Day 2: LIKE, IN, BETWEEN, JOINs and related SQL


-- ============================================================
-- 1. LIKE
-- ============================================================

SELECT *
FROM customers
WHERE customer_name LIKE 'A%';

SELECT *
FROM customers
WHERE customer_name LIKE '%A%';

SELECT *
FROM customers
WHERE customer_name LIKE '%en';


-- ============================================================
-- 2. ILIKE
-- ============================================================

SELECT *
FROM customers
WHERE customer_name ILIKE '%A%';


-- ============================================================
-- 3. UNDERSCORE (_) WILDCARD
-- ============================================================

SELECT *
FROM customers
WHERE city LIKE 'L_nd__';


-- ============================================================
-- 4. IN
-- ============================================================

SELECT *
FROM customers
WHERE country IN ('Germany', 'France', 'UK');


-- ============================================================
-- 5. NOT IN
-- ============================================================

SELECT *
FROM customers
WHERE country NOT IN ('Germany', 'France', 'UK');


-- ============================================================
-- 6. IN WITH SUBQUERY
-- ============================================================

SELECT *
FROM customers
WHERE customer_id IN (
    SELECT customer_id
    FROM orders
);


-- ============================================================
-- 7. NOT IN WITH SUBQUERY
-- ============================================================

SELECT *
FROM customers
WHERE customer_id NOT IN (
    SELECT customer_id
    FROM orders
);


-- ============================================================
-- 8. BETWEEN
-- ============================================================

SELECT *
FROM products
WHERE price BETWEEN 10 AND 15;

SELECT *
FROM products
WHERE product_name BETWEEN 'Pavlova' AND 'Tofu';

SELECT *
FROM orders
WHERE order_date BETWEEN '2023-04-12' AND '2023-05-05';


-- ============================================================
-- 9. ALIASES
-- ============================================================

SELECT customer_id AS id
FROM customers;

SELECT customer_id id
FROM customers;


-- ============================================================
-- 10. CONCATENATE COLUMNS
-- ============================================================

SELECT product_name || unit AS product
FROM products;

SELECT product_name AS "My Great Products"
FROM products;


-- ============================================================
-- 11. CONSUMER TABLE FOR JOIN PRACTICE
-- ============================================================

-- Use the same consumer table you created during Day 2.
-- If your actual table definition is different, keep your
-- original definition from PostgreSQL here.


-- ============================================================
-- 12. INNER JOIN - CARS + CONSUMER
-- ============================================================

-- Example structure:
-- SELECT cars.brand, cars.model, consumer.consumer_name
-- FROM cars
-- INNER JOIN consumer
--     ON cars.consumer_id = consumer.consumer_id;


-- ============================================================
-- 13. LEFT JOIN - CARS + CONSUMER
-- ============================================================

-- Example structure:
-- SELECT cars.brand, cars.model, consumer.consumer_name
-- FROM cars
-- LEFT JOIN consumer
--     ON cars.consumer_id = consumer.consumer_id;


-- ============================================================
-- 14. RIGHT JOIN - CARS + CONSUMER
-- ============================================================

-- Example structure:
-- SELECT cars.brand, cars.model, consumer.consumer_name
-- FROM cars
-- RIGHT JOIN consumer
--     ON cars.consumer_id = consumer.consumer_id;


-- ============================================================
-- 15. FULL JOIN - CARS + CONSUMER
-- ============================================================

-- Example structure:
-- SELECT cars.brand, cars.model, consumer.consumer_name
-- FROM cars
-- FULL JOIN consumer
--     ON cars.consumer_id = consumer.consumer_id;



-- ============================================================
-- 17. UNION
-- ============================================================

SELECT product_id, product_name
FROM products
UNION
SELECT testproduct_id, product_name
FROM testproducts
ORDER BY product_id;


-- ============================================================
-- 18. UNION ALL
-- ============================================================

SELECT product_id
FROM products
UNION ALL
SELECT testproduct_id
FROM testproducts
ORDER BY product_id;
