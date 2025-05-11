SELECT
    CONCAT(e.first_name, ' ', e.last_name) AS full_name,
    TIMESTAMPDIFF(YEAR, e.date_of_birth, CURDATE()) AS age,
    d.department_name,
    s.salary
FROM
    salaries s
JOIN
    employees e ON s.employee_id = e.employee_id
JOIN
    departments d ON e.department_id = d.department_id
WHERE
    DAY(s.transaction_date) != 1
    AND s.salary = (
        SELECT MAX(salary)
        FROM salaries
        WHERE employee_id = s.employee_id
          AND DAY(transaction_date) != 1
    );
