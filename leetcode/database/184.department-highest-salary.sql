-- https://leetcode.com/problems/department-highest-salary/
-- Runtime: 907 ms, faster than 65.54% of Oracle online submissions for Department Highest Salary.
-- Memory Usage: 0B, less than 100.00% of Oracle online submissions for Department Highest Salary.
-- Write your PL/SQL query statement below

select d.name as Department ,
d1.name as Employee,
d1.salary
From ( select e.departmentid,
e.name,
e.salary ,
rank() over (partition by departmentid order by salary desc) rn
From employee e) d1 ,
department d
where rn = 1
and d.id = d1.departmentid;