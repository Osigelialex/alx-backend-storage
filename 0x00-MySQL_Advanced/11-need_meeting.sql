-- script that creates a view need_meeting that lists all students that 
-- have a score under 80 (strict) and no last_meeting or more than 1 month.
CREATE VIEW need_meeting
AS
SELECT * FROM students WHERE score < 80 AND 
(last_meeting = NULL OR MONTH(last_meeting) = MONTH(NOW() - INTERVAL 2 MONTH));
