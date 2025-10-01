SELECT 
    EXTRACT(HOUR FROM orderdate) AS order_hour,
    COUNT(orderid) AS orders_placed,
    SUM(balancespent) AS total_sales
FROM Orders
GROUP BY order_hour
ORDER BY order_hour;
