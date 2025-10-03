-- Special Query #3: Peak Sales Day

SELECT 
    CAST(orderdate AS DATE) AS order_day,
    SUM(balancespent) AS daily_sales
FROM Customers
GROUP BY order_day
ORDER BY daily_sales DESC
LIMIT 10;
