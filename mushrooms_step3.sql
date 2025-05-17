-- 1. Уникальные регионы сбора грибов
SELECT DISTINCT name FROM Regions;

-- 2. Название, сезон, съедобность грибов из категории "Трубчатые"
SELECT m.name, m.season, m.edible
FROM Mushrooms m
JOIN Categories c ON m.category_id = c.category_id
WHERE c.name = 'Трубчатые';

-- 3. Количество грибов по категориям, сортировка по убыванию
SELECT c.name AS category_name, COUNT(*) AS mushroom_count
FROM Mushrooms m
JOIN Categories c ON m.category_id = c.category_id
GROUP BY c.name
ORDER BY mushroom_count DESC;

-- 4. Название и описание съедобных грибов в 5 самых больших регионах
SELECT m.name, m.description
FROM Mushrooms m
JOIN Regions r ON m.primary_region_id = r.region_id
WHERE m.edible = TRUE
ORDER BY r.size DESC
LIMIT 5;

-- 5. Названия грибов, которые растут весной, в категории "Пластинчатые", в регионах до 6000
SELECT m.name
FROM Mushrooms m
JOIN Categories c ON m.category_id = c.category_id
JOIN Regions r ON m.primary_region_id = r.region_id
WHERE m.season = 'весна'
  AND c.name = 'Пластинчатые'
  AND r.size <= 6000;