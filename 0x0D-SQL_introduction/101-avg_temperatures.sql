-- a script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending)
SOURCE temperatures.sql;
SELECT city, AVG(VALUE) AS  avg_temp ORDER BY avg_temp DESC;
