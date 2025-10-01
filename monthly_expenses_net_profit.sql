SELECT  
    EXTRACT(YEAR FROM startdate) AS sales_year,
    EXTRACT(MONTH FROM startdate) AS sales_month,
    CASE
        WHEN EXTRACT(MONTH FROM startdate) = 1 THEN 'January'
        WHEN EXTRACT(MONTH FROM startdate) = 2 THEN 'February'
        WHEN EXTRACT(MONTH FROM startdate) = 3 THEN 'March'
        WHEN EXTRACT(MONTH FROM startdate) = 4 THEN 'April'
        WHEN EXTRACT(MONTH FROM startdate) = 5 THEN 'May'
        WHEN EXTRACT(MONTH FROM startdate) = 6 THEN 'June'
        WHEN EXTRACT(MONTH FROM startdate) = 7 THEN 'July'
        WHEN EXTRACT(MONTH FROM startdate) = 8 THEN 'August'
        WHEN EXTRACT(MONTH FROM startdate) = 9 THEN 'September'
        WHEN EXTRACT(MONTH FROM startdate) = 10 THEN 'October'
        WHEN EXTRACT(MONTH FROM startdate) = 11 THEN 'November'
                ELSE 'December'
    END AS season,
    SUM(totalexpenses)::numeric::money AS monthlyexpenses,
    SUM(totalsales-totalexpenses)::numeric::money as net_profit
FROM profits
GROUP BY sales_year, sales_month, season
ORDER BY sales_year, sales_month;