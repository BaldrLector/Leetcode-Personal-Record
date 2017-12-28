
SELECT max(Salary) as SecondHighestSalary
From Employee
WHERE Salary not in (SELECT max(Salary)
FROM Employee )

-- select (
--   select distinct Salary
--     from Employee
--     order by Salary Desc limit 1 offset
-- 1
-- )as second