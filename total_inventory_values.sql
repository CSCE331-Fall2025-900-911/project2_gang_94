--finds the total inventory value of on hand inventory
SELECT SUM(quantity * cost) AS total_value
FROM onhandinventory;