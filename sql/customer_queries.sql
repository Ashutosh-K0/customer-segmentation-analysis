-- =========================================
-- Customer Segmentation Analysis Queries
-- =========================================

-- View Complete Dataset
SELECT *
FROM customers;

-- View First 10 Customers
SELECT *
FROM customers
LIMIT 10;

-- Total Number of Customers
SELECT COUNT(*) AS total_customers
FROM customers;

-- Average Age of Customers
SELECT AVG(age) AS average_age
FROM customers;

-- Average Annual Income
SELECT AVG(annual_income) AS average_income
FROM customers;

-- Average Spending Score
SELECT AVG(spending_score) AS average_spending_score
FROM customers;

-- Customer Distribution by Gender
SELECT 
    gender,
    COUNT(*) AS total_customers
FROM customers
GROUP BY gender;

-- Average Spending by Gender
SELECT 
    gender,
    AVG(spending_score) AS average_spending
FROM customers
GROUP BY gender;

-- Average Income by Gender
SELECT 
    gender,
    AVG(annual_income) AS average_income
FROM customers
GROUP BY gender;

-- Highest Income Customers
SELECT *
FROM customers
ORDER BY annual_income DESC
LIMIT 10;

-- Highest Spending Customers
SELECT *
FROM customers
ORDER BY spending_score DESC
LIMIT 10;

-- Lowest Spending Customers
SELECT *
FROM customers
ORDER BY spending_score ASC
LIMIT 10;

-- Average Income by Age
SELECT 
    age,
    AVG(annual_income) AS avg_income
FROM customers
GROUP BY age
ORDER BY avg_income DESC;

-- Average Spending Score by Age
SELECT 
    age,
    AVG(spending_score) AS avg_spending
FROM customers
GROUP BY age
ORDER BY avg_spending DESC;

-- Customers with High Income and High Spending
SELECT *
FROM customers
WHERE annual_income > 70
AND spending_score > 70;

-- Customers with High Income but Low Spending
SELECT *
FROM customers
WHERE annual_income > 70
AND spending_score < 40;

-- Customers with Low Income but High Spending
SELECT *
FROM customers
WHERE annual_income < 40
AND spending_score > 70;

-- Customers Between Age 20 and 30
SELECT *
FROM customers
WHERE age BETWEEN 20 AND 30;

-- Top 5 Youngest Customers
SELECT *
FROM customers
ORDER BY age ASC
LIMIT 5;

-- Top 5 Oldest Customers
SELECT *
FROM customers
ORDER BY age DESC
LIMIT 5;

-- Income Category Analysis
SELECT
    CASE
        WHEN annual_income < 40 THEN 'Low Income'
        WHEN annual_income BETWEEN 40 AND 70 THEN 'Medium Income'
        ELSE 'High Income'
    END AS income_category,
    COUNT(*) AS customer_count
FROM customers
GROUP BY income_category;

-- Spending Score Category Analysis
SELECT
    CASE
        WHEN spending_score < 40 THEN 'Low Spending'
        WHEN spending_score BETWEEN 40 AND 70 THEN 'Medium Spending'
        ELSE 'High Spending'
    END AS spending_category,
    COUNT(*) AS customer_count
FROM customers
GROUP BY spending_category;

-- Combined Income and Spending Segmentation
SELECT
    CASE
        WHEN annual_income > 70 AND spending_score > 70
            THEN 'Premium Customers'

        WHEN annual_income > 70 AND spending_score < 40
            THEN 'Careful Customers'

        WHEN annual_income < 40 AND spending_score > 70
            THEN 'Impulsive Customers'

        ELSE 'Standard Customers'
    END AS customer_segment,
    
    COUNT(*) AS total_customers
FROM customers
GROUP BY customer_segment;

-- Average Spending Score by Customer Segment
SELECT
    CASE
        WHEN annual_income > 70 AND spending_score > 70
            THEN 'Premium Customers'

        WHEN annual_income > 70 AND spending_score < 40
            THEN 'Careful Customers'

        WHEN annual_income < 40 AND spending_score > 70
            THEN 'Impulsive Customers'

        ELSE 'Standard Customers'
    END AS customer_segment,

    AVG(spending_score) AS avg_spending
FROM customers
GROUP BY customer_segment;

-- Premium Female Customers
SELECT *
FROM customers
WHERE gender = 'Female'
AND annual_income > 70
AND spending_score > 70;

-- Premium Male Customers
SELECT *
FROM customers
WHERE gender = 'Male'
AND annual_income > 70
AND spending_score > 70;