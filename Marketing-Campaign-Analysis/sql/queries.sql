-- sql/queries.sql

-- 1. Overall response rate
SELECT AVG(y) AS response_rate FROM campaign_data;

-- 2. Response by age group
SELECT age_group, AVG(y) AS response_rate
FROM campaign_data
GROUP BY age_group;

-- 3. Campaign effectiveness
SELECT campaign, AVG(y) AS response_rate
FROM campaign_data
GROUP BY campaign
ORDER BY response_rate DESC;

-- 4. Previous campaign success
SELECT poutcome_success, AVG(y) AS response_rate
FROM campaign_data
GROUP BY poutcome_success;

-- 5. Overall Response Rate
SELECT ROUND(AVG(y)*100, 2) AS response_rate_percent
FROM campaign_data;

-- 6. Response by Job
SELECT job_admin, AVG(y) as response_rate
FROM campaign_data
GROUP BY job_admin
ORDER BY response_rate DESC;

-- 7. Response by Age Group
SELECT age_group, AVG(y) as response_rate
FROM campaign_data
GROUP BY age_group
ORDER BY response_rate DESC;

-- 8. Campaign Efficiency
SELECT campaign, AVG(y) as response_rate
FROM campaign_data
GROUP BY campaign
ORDER BY response_rate DESC;

-- 9. Previous Campaign Success Impact
SELECT poutcome_success, AVG(y) as response_rate
FROM campaign_data
GROUP BY poutcome_success;