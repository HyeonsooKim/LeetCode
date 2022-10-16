# Write your MySQL query statement below
SELECT e.event_day 'day', e.emp_id 'emp_id', SUM(e.out_time-e.in_time) 'total_time'
FROM Employees e
GROUP BY e.event_day, e.emp_id