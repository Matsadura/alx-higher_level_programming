-- Lists the all the records of the talbe second_table
-- Doesn't list rows without a name
SELECT score, name
FROM second_table
WHERE name != ''
ORDER BY score DESC;
