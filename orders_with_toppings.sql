SELECT
    month,
    ROUND(AVG(orders_per_month)::numeric, 2) AS avg_toppings_orders
FROM (
    SELECT
        EXTRACT(YEAR FROM orderdate) AS year,
        EXTRACT(MONTH FROM orderdate) AS month,
        COUNT(*) AS orders_per_month
    FROM customers
    WHERE itemsused LIKE '%add%'
    GROUP BY year, month
) AS monthly_count
GROUP BY month
ORDER BY month;