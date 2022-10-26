# Write your MySQL query statement below
SELECT u.name NAME, SUM(t.amount) BALANCE
FROM Users u
    JOIN Transactions t ON u.account = t.account
GROUP BY t.account
HAVING BALANCE > 10000