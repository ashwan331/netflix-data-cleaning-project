-- Total Movies vs TV Shows
SELECT type, COUNT(*) AS total
FROM netflix_titles
GROUP BY type;

-- Top 10 Countries
SELECT country, COUNT(*) AS total
FROM netflix_titles
GROUP BY country
ORDER BY total DESC
LIMIT 10;

-- Most Common Ratings
SELECT rating, COUNT(*) AS total
FROM netflix_titles
GROUP BY rating
ORDER BY total DESC;

-- Content Added Per Year
SELECT year_added, COUNT(*) AS total
FROM netflix_titles
GROUP BY year_added
ORDER BY year_added;

-- Top Directors
SELECT director, COUNT(*) AS total
FROM netflix_titles
GROUP BY director
ORDER BY total DESC
LIMIT 10;