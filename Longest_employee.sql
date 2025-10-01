--query the find the longest working employee for day 
SELECT name, schedule_date, hours_worked, customers_served
FROM Employees e1
WHERE hours_worked = (
    SELECT MAX(hours_worked)
    FROM Employees e2
    WHERE e1.name = e2.name
);
