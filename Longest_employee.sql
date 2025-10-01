--query the find the longest working employee for day 
SELECT employee_id, schedule_date, hours_worked, customers_served
FROM Employees
--WHERE schedule_date = '2024-10-01' -- if we do specific date 
WHERE hours_worked = (
    SELECT MAX(hours_worked)
    FROM Employees 
--  WHERE schedule_date = '2024-10-01'
);
