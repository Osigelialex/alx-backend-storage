-- ranks country origin by bands
SELECT origin, COUNT(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY COUNT(fans) DESC;
