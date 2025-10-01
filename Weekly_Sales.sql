SELECT 
    EXTRACT(YEAR FROM orderdate) AS year,
    EXTRACT(WEEK FROM orderdate) AS week_number,
    COUNT(orderid) AS orders_placed
FROM Customers
GROUP BY year, week_number
ORDER BY year, week_number;
