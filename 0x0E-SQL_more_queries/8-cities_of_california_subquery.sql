-- Task 8
-- Select cities of State id = 1
SELECT id, name FROM cities WHERE state_id in (SELECT id FROM states WHERE id = 1);
