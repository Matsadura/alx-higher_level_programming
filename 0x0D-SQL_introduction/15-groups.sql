-- Lists the number of records with the same score in the table second_table
SELECT score,
COUNT(SCORE)
AS number
FROM second_table
GROUP BY score
ORDER BY score DESC;
