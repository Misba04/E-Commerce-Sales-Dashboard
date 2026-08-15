-- 1. Total Sales
SELECT SUM(Amount) AS Total_Sales
FROM sales;

-- 2. Total Orders
SELECT COUNT(DISTINCT "Order ID") AS Total_Orders
FROM sales;

-- 3. Average Order Value
SELECT AVG(Amount) AS Average_Order_Value
FROM sales;

-- 4. Sales by Category
SELECT Category, SUM(Amount) AS Total_Sales
FROM sales
GROUP BY Category
ORDER BY Total_Sales DESC;

-- 5. Sales by Fulfilment
SELECT Fulfilment, SUM(Amount) AS Total_Sales
FROM sales
GROUP BY Fulfilment
ORDER BY Total_Sales DESC;

-- 6. Sales by State
SELECT "ship-state", SUM(Amount) AS Total_Sales
FROM sales
GROUP BY "ship-state"
ORDER BY Total_Sales DESC
LIMIT 10;

-- 7. Sales by City
SELECT "ship-city", SUM(Amount) AS Total_Sales
FROM sales
GROUP BY "ship-city"
ORDER BY Total_Sales DESC
LIMIT 10;