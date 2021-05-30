-- Runtime: 413 ms, faster than 84.07% of Oracle online submissions for Second Highest Salary.
-- Memory Usage: 0B, less than 100.00% of Oracle online submissions for Second Highest Salary.
-- Write your PL/SQL query statement below
SELECT
    (
        SELECT
            salary AS sal
        FROM
            (
                SELECT DISTINCT
                    salary,
                    DENSE_RANK()
                    OVER(
                        ORDER BY salary DESC
                    ) AS rank
                FROM
                    employee
            )
        WHERE
            rank = 2
    ) AS secondhighestsalary
FROM
    dual;

