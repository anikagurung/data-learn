--Write a SQL statement to prepare a list with salesman name, customer name and their cities for the salesmen and customer who belongs to the same city.

SELECT
    s.name AS salesman_name,
    c.cust_name AS customer_name
FROM salesman s
JOIN customer c
ON s.salesman_id = c.salesman_id;



--Write a SQL statement to know which salesman are working for which customer.

SELECT
    s.name AS salesman_name,
    c.cust_name AS customer_name
FROM salesman s
JOIN customer c
ON s.salesman_id = c.salesman_id;



--Write a SQL statement to make a list with order no, purchase amount, customer name and their cities for those orders which order amount between 500 and 2000.

SELECT
    o.ord_no,
    o.purch_amt,
    c.cust_name,
    c.city
FROM orders o
JOIN customer c
ON o.customer_id = c.customer_id
WHERE o.purch_amt BETWEEN 500 AND 2000;



--Write a SQL statement to find the list of customers who appointed a salesman for their jobs who gets a commission from the company is more than 12%.

SELECT
    c.cust_name AS customer_name,
    s.name AS salesman_name,
    s.commission
FROM customer c
JOIN salesman s
ON c.salesman_id = s.salesman_id
WHERE s.commission > 0.12;



--Write a SQL statement to find the list of customers who appointed a salesman for their jobs who does not live in the same city where their customer lives, and gets a commission above 12% .

SELECT  c.cust_name AS customer_name,
    c.city AS customer_city,
    s.name AS salesman_name,
    s.city AS salesman_city,
    s.commission FROM customer c JOIN salesman s ON c.salesman_id = s.salesman_id
WHERE c.city <> s.city AND s.commission > 0.12;



