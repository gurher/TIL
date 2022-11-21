WITH final AS (
  SELECT 
    manufacturer,
    units_sold,
    drug,
    ROW_NUMBER() OVER(PARTITION BY manufacturer ORDER BY units_sold DESC) rwn
    
  FROM pharmacy_sales
      )
      
SELECT
  manufacturer,
  drug AS top_drugs
FROM final
WHERE rwn < 3
ORDER BY 1
