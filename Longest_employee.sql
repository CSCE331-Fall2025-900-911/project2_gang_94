--query the find the longest working employee every day  
SELECT name, schedule_date, hours_worked
FROM Employees e1
WHERE hours_worked = (
    SELECT MAX(hours_worked)
    FROM Employees e2
    WHERE e2.schedule_date = e1.schedule_date);


