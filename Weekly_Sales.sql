SELECT 
    YEAR(orderdate) AS year,
    WEEK(orderdate, 1) AS week_number,   -- mode=1 means weeks start on Monday
    COUNT(orderid) AS orders_placed
FROM Orders
GROUP BY year, week_number
ORDER BY year, week_number;
