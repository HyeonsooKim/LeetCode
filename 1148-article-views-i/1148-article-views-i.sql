# Write your MySQL query statement below
SELECT DISTINCT t.author_id as id
FROM (SELECT *
FROM Views
WHERE author_id = viewer_id) as t
ORDER BY t.author_id