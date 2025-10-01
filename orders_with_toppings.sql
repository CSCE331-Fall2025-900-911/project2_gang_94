SELECT
    AVG(orders_per_month) AS avg_toppings_orders
FROM (
    SELECT
        EXTRACT(YEAR FROM orderdate) AS year,
        EXTRACT(MONTH FROM orderdate) AS month,
        COUNT(*) AS orders_per_month
    FROM customers
    WHERE itemsused LIKE '%(%'
    GROUP BY year, month
) AS monthly_count;