-- lists all bands with Glam rock as their main style, ranked by their longevity
SELECT band_name, COALESCE(split, 2022) - formed AS longetivity
FROM metal_bands
ORDER BY longetivity DESC;
