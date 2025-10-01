SELECT 
    EXTRACT(HOUR FROM orderdate) AS order_hour,
    COUNT(orderid) AS orders_placed,
    SUM(balancespent) AS total_sales
FROM Customers
GROUP BY order_hour
ORDER BY order_hour;
