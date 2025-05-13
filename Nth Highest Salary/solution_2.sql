CREATE OR REPLACE FUNCTION NthHighestSalary(N INT) RETURNS TABLE (Salary INT) AS $$
BEGIN
  RETURN QUERY (
    SELECT CASE
        WHEN N > 0 THEN COALESCE((SELECT DISTINCT Employee.salary
                        FROM Employee
                        ORDER BY salary DESC
                        LIMIT 1 OFFSET N-1), NULL) 
        ELSE NULL
    END AS getNthHighestSalary
    
      
  );
END;
$$ LANGUAGE plpgsql;