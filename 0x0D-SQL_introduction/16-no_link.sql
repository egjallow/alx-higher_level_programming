-- List all records from second_table with a name value, showing score and name, ordered by score descending
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
