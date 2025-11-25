# Write your MySQL query statement below
WITH cte AS
(SELECT *, DATE_ADD(recordDate, INTERVAL -1 DAY) AS yesterday,LAG(recordDate) OVER (ORDER BY recordDate) as prev_date, LAG(temperature) OVER(ORDER BY  recordDate) as prev_temp
FROM Weather )
SELECT id 
FROM cte
WHERE yesterday=prev_date AND temperature>prev_temp