SELECT DISTINCT "name", SUM(customers_served) AS customers_served
FROM employees GROUP BY "name";
