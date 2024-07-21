-- Write query to get number of graded assignments for each student:
select student_id, COUNT(*) from assignments WHERE state = 'GRADED' GROUP BY student_id; 
