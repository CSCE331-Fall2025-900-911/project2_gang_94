SELECT DISTINCT employees."Employee ID", customers_served, "Hours Worked", 
SUM(balancespent) / NULLIF(COUNT(DISTINCT customers.orderid), 0) AS ratio 
FROM employees 

JOIN customers ON employees."Employee ID" = customers."Employee ID" 
WHERE orderdate BETWEEN @StartDate AND @EndDate 

GROUP BY "Employee ID" 
ORDER BY ratio DESC;