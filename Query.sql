-- Neighborhood ordered by population density
WITH temp as (
SELECT Neighborhood.name, Density.density
FROM Neighborhood
JOIN Density on Neighborhood.id = Density.id
),
temp2 as (
SELECT COUNT(Crime.id) as NumCrimes, Neighborhood.name
FROM Crime
JOIN Neighborhood on Crime.neighborhoodId = Neighborhood.id
GROUP by Neighborhood.name
)
SELECT temp.name, temp.density, temp2.NumCrimes
FROM temp
JOIN temp2 on temp.name = temp2.name
ORDER BY temp2.NumCrimes desc