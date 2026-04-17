--  Total Revenue
SELECT SUM(Revenue) AS Total_Revenue FROM sales;

-- Revenue by Region
SELECT Region, SUM(Revenue) AS Revenue
FROM sales
GROUP BY Region;

-- Top Sales Rep
SELECT Sales_Rep, SUM(Revenue) AS Revenue
FROM sales
GROUP BY Sales_Rep
ORDER BY Revenue DESC;