-- Employee Details
SELECT  emp.emp_no, emp.last_name, emp.first_name, emp.gender, sal.salary
FROM public."Employees" as emp
    JOIN public."Salaries" as sal
    ON (emp.emp_no = sal.emp_no)
ORDER BY emp.emp_no;

-- Employees hired in 1986
SELECT first_name, last_name, hire_date FROM public."Employees"
WHERE hire_date BETWEEN '1986-01-01' AND '1986-12-31';

-- Manager of each Department
SELECT  dm.emp_no, emp.last_name, emp.first_name, dm.dept_no, dept.dept_name, dm.from_date, dm.to_date
FROM public."Dept_manager" AS Dm
    INNER JOIN public."Departments" AS dept
        ON (dm.dept_no = dept.dept_no)
    INNER JOIN public."Employees" AS emp
        ON (dm.emp_no = emp.emp_no);
		
-- Employee Departments
SELECT  emp.emp_no, emp.last_name, emp.first_name, dept.dept_name
FROM public."Employees" AS emp
    INNER JOIN public."Dept_emp" AS De
        ON (emp.emp_no = De.emp_no)
    INNER JOIN public."Departments" AS dept
        ON (De.dept_no = dept.dept_no)
ORDER BY emp.emp_no;

-- Employess with first name Hercules and last name that starts with a B
SELECT * FROM public."Employees"
WHERE first_name = 'Hercules'
AND last_name LIKE 'B%';

-- All Employees in Sales Department
SELECT  emp.emp_no, emp.last_name, emp.first_name, dept.dept_name
FROM public."Employees" AS emp
    INNER JOIN public."Dept_emp" AS De
        ON (emp.emp_no = De.emp_no)
    INNER JOIN public."Departments" AS dept
        ON (De.dept_no = dept.dept_no)
WHERE dept.dept_name = 'Sales'
ORDER BY emp.emp_no;

-- All Employees in Sales And Development Departments
SELECT  emp.emp_no, emp.last_name, emp.first_name, dept.dept_name
FROM public."Employees" AS emp
    INNER JOIN public."Dept_emp" AS De
        ON (emp.emp_no = De.emp_no)
    INNER JOIN public."Departments" AS dept
        ON (De.dept_no = dept.dept_no)
WHERE dept.dept_name IN ('Sales', 'Development')
ORDER BY emp.emp_no;

-- Frequency Count of Employee Last Names
SELECT last_name, COUNT(last_name)
FROM public."Employees"
GROUP BY last_name
ORDER BY COUNT(last_name) DESC;






