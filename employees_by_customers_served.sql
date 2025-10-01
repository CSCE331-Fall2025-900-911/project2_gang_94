SELECT DISTINCT employees.employee_id, "name", customers_served, hours_worked, 
SUM(balancespent) / NULLIF(COUNT(DISTINCT customers.orderid), 0) AS ratio 
FROM employees 

JOIN customers ON employees.employee_id = customers.employee_id 
WHERE orderdate BETWEEN "2024-10-01" AND "2025-03-01" 

GROUP BY employee_id 
ORDER BY ratio DESC;