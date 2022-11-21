WITH table1 AS (
    SELECT 
      DISTINCT sender.payer_id, sender.recipient_id
    FROM payments sender
    INNER JOIN payments receiver
      ON sender.payer_id = receiver.recipient_id
      AND sender.recipient_id = receiver.payer_id
    ORDER BY 1
    ),
  
final AS (
  SELECT 
    payer_id,
    recipient_id,
    -- SUM(1) OVER(),
    ROW_NUMBER() OVER(ORDER BY payer_Id) AS rwn
  FROM table1
    )

SELECT MAX(rwn)/2
FROM final


-- WITH relationships AS (
-- SELECT payer_id, recipient_id
-- FROM payments
-- INTERSECT
-- SELECT recipient_id, payer_id
-- FROM payments)

-- SELECT COUNT(payer_id) / 2 AS unique_relationships
-- FROM relationships;