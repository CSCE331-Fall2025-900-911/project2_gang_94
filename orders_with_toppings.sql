SELECT
    EXTRACT(MONTH FROM orderdate) AS month,
    COUNT(*)
FROM customers
WHERE itemsused LIKE '%add%'
GROUP BY month
ORDER BY month;