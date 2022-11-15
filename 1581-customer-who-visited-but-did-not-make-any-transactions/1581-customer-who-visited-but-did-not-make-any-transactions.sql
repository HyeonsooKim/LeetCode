# Write your MySQL query statement below
SELECT v.customer_id, count(v.visit_id) count_no_trans
FROM Visits v
LEFT OUTER JOIN Transactions t ON v.visit_id = t.visit_id
WHERE t.visit_id is NULL
GROUP BY v.customer_id