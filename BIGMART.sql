-- SELECT COUNT(*) FROM dbo.[bigmart-data-MAIN] 

-- WHERE outlet_size IS NULL
-- SET ANSI_WARNINGS OFF
-- GO

-- UPDATE dbo.[bigmart-data-MAIN]

-- SET item_weight = B.max_weight

-- FROM dbo.[bigmart-data-MAIN] A 

-- INNER JOIN (
--     SELECT item_identifier, MAX(item_weight) AS max_weight

--     FROM dbo.[bigmart-data-MAIN]
--     GROUP BY item_identifier
-- ) B ON A.item_identifier = B.item_identifier

-- WHERE A.item_weight IS NULL

-- SELECT * FROM dbo.[bigmart-data-MAIN]

-- WHERE item_weight IS NULL

-- SELECT 
--     DISTINCT(outlet_identifier)

-- FROM
--  dbo.[bigmart-data-MAIN]  
--  WHERE outlet_size IS NULL


-- SELECT 
--     *

-- FROM
--  dbo.[bigmart-data-MAIN]  
--  WHERE outlet_identifier =  'OUT010'
-- -- WHERE outlet_size IS NULL


-- SELECT 

--     outlet_location_type,
--     outlet_type,
--     outlet_size,
--     COUNT(outlet_size)

-- FROM 
--     dbo.[bigmart-data-MAIN]

-- GROUP BY outlet_location_type, outlet_type, outlet_size
-- ORDER BY outlet_location_type, outlet_type, outlet_size, COUNT(outlet_size )


SELECT @@SERVERNAME