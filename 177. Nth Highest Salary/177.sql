CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    RETURN (
    -- Write your MySQL query statement below.
    select distinct e1.salary
    from Employee e1
    where N-1 = (select count(distinct e2.Salary)
    from Employee e2
    where e1.Salary < e2.Salary)
    -- SELECT DISTINCT Salary FROM Employee ORDER BY Salary DESC LIMIT N-1, 1
  );
END