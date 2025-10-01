SELECT
    EXTRACT(YEAR FROM orderdate) AS year,
    EXTRACT(MONTH FROM orderdate) AS month,
    COUNT(*)
FROM customers
WHERE itemsused LIKE '%add%'
GROUP BY year, month
ORDER BY month;