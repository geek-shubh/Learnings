-- https://leetcode.com/problems/combine-two-tables/
-- Runtime: 840 ms, faster than 14.62% of Oracle online submissions for Combine Two Tables.
-- Memory Usage: 0B, less than 100.00% of Oracle online submissions for Combine Two Tables.

-- Write your PL/SQL query statement below
select FirstName, LastName, City, State
from Person P
left join Address A
on
P.PersonId = A.PersonId;