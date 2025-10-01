SELECT
    CASE
        WHEN EXTRACT(MONTH FROM startdate) IN (12, 1, 2) THEN 'Winter'
        WHEN EXTRACT(MONTH FROM startdate) IN (3, 4, 5) THEN 'Spring'
        WHEN EXTRACT(MONTH FROM startdate) IN (6, 7, 8) THEN 'Summer'
        ELSE 'Fall'
    END AS season,
    SUM(totalsales-totalexpenses)::numeric::money as profit
FROM profits
GROUP BY season
ORDER BY profit;