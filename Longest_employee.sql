--query the find the longest working employee every day  
SELECT "Employee ID", schedule_date, "Hours Worked", customers_served
FROM Employees e1
WHERE "Hours Worked" = 
    SELECT MAX("Hours Worked")
    FROM Employees e2
    WHERE e2.schedule_date = e1.schedule_date

