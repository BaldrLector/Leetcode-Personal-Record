# Write your
MySQL query statement below
select a.Name as 'Employee'
from Employee a, Employee b
where b.Id=a.ManagerId and a.Salary>b.Salary 