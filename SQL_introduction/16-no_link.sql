-- list records in a table provided there is no NULL value
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
