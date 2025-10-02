SELECT
    '2024-12-25' AS peak_day,
    SUM(CASE WHEN DATE(orderdate) = '2024-12-25' THEN balancespent ELSE 0 END)::numeric::money AS peak_sale,
    (SELECT
        AVG(daily_sales)::numeric::money
    FROM (
        SELECT
            DATE(orderdate) AS day,
            SUM(balancespent) AS daily_sales
        FROM Customers
        GROUP BY day
    ) t)::money AS daily_totals
FROM customers;