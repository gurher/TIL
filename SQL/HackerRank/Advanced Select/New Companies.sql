
SELECT 
        c.company_code
       , c.founder
       , COUNT(DISTINCT l.lead_manager_code) 
       , COUNT(DISTINCT s.senior_manager_code)
       , COUNT(DISTINCT m.manager_code)
       , COUNT(DISTINCT e.employee_code)
FROM company c
LEFT JOIN lead_manager l
    ON c.company_code = l.company_code
LEFT JOIN senior_manager s
    ON c.company_code = s.company_code 
LEFT JOIN manager m
    ON c.company_code = m.company_code
LEFT JOIN employee e
    ON c.company_code = e.company_code
GROUP BY c.company_code, c.founder
    

-- HackerRank Problem
-- SQL Solution
-- By: Thomas-George-T

-- SELECT 
--     c.company_code,
--     c.founder,
--     count(distinct lm.lead_manager_code),
--     count(distinct sm.senior_manager_code),
--     count(distinct m.manager_code), 
--     count(distinct e.employee_code)
-- FROM Company c, Lead_Manager lm, Senior_Manager sm, Manager m, Employee e
-- WHERE
-- c.company_code=lm.company_code AND
-- lm.lead_manager_code=sm.lead_manager_code AND
-- sm.senior_manager_code=m.senior_manager_code AND
-- m.manager_code=e.manager_code
-- GROUP BY c.company_code,c.founder
-- ORDER BY c.company_code ASC