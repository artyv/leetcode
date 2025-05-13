CREATE OR REPLACE FUNCTION NthHighestSalary(N INT) RETURNS TABLE (Salary INT) AS $$
BEGIN
  RETURN QUERY (
    SELECT COALESCE((SELECT DISTINCT Employee.salary
        FROM Employee
        ORDER BY salary DESC
        LIMIT 1 OFFSET N-1), NULL
    ) AS getNthHighestSalary
    
      
  );
END;
$$ LANGUAGE plpgsql;