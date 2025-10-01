SELECT 
    EXTRACT(YEAR FROM startdate) AS year,
    EXTRACT(MONTH FROM startdate) AS month,
    ROUND((totalsales - totalexpenses)::numeric,2) AS monthprofit
FROM profits
ORDER BY monthprofit DESC;