--DATA ANALYSIS
--List the following details of each employee: employee number, last name, first name, sex, and salary.
SELECT e.emp_no AS "employee number",e.last_name AS "last name",e.first_name AS "first name",e.sex,s.salary
FROM employees AS e
INNER JOIN salaries AS s
ON e.emp_no = s.emp_no;

--List first name, last name, and hire date for employees who were hired in 1986.
SELECT first_name AS "first name", last_name AS "last name", hire_date AS "hire date in month/date/year"
FROM employees
WHERE hire_date LIKE '%1986';

--List the manager of each department with the following information: department number, department name, 
--the manager's employee number, last name, first name.
SELECT d.dept_no AS "department number", d.dept_name AS "department name", e.emp_no AS "manager employee number", 
	e.last_name AS "last name", e.first_name AS "first name"
FROM departments AS d
INNER JOIN dept_manager AS m 
ON d.dept_no = m.dept_no
INNER JOIN employees AS e
ON e.emp_no = m.emp_no;

	
--List the department of each employee with the following information: employee number, last name, first name, and department name.
SELECT e.emp_no AS "employee name", e.last_name AS "last name", e.first_name AS "first name", d.dept_name AS "department name"
FROM departments AS d
INNER JOIN dept_emp AS d_e
ON d.dept_no = d_e.dept_no
INNER JOIN employees AS e
ON e.emp_no = d_e.emp_no;

--List first name, last name, and sex for employees whose first name is "Hercules" and last names begin with "B."
SELECT first_name AS "first name", last_name AS "last name", sex
FROM employees
WHERE first_name = 'Hercules' 
AND last_name LIKE 'B%';


--List all employees in the Sales department, including their employee number, last name, first name, and department name.
SELECT e.emp_no AS "employee name", e.last_name AS "last name", e.first_name AS "first name", d.dept_name AS "department name"
FROM departments AS d
INNER JOIN dept_emp AS d_e
ON d.dept_no = d_e.dept_no
INNER JOIN employees AS e
ON e.emp_no = d_e.emp_no
WHERE d.dept_name = 'Sales';

--List all employees in the Sales and Development departments, including their employee number, last name, first name, 
--and department name.
SELECT e.emp_no AS "employee name", e.last_name AS "last name", e.first_name AS "first name", d.dept_name AS "department name"
FROM departments AS d
FROM departments AS d
INNER JOIN dept_emp AS d_e
ON d.dept_no = d_e.dept_no
INNER JOIN employees AS e
ON e.emp_no = d_e.emp_no
WHERE d.dept_name IN ('Sales','Development');

--In descending order, list the frequency count of employee last names, i.e., how many employees share each last name.
SELECT last_name AS "last name", COUNT(last_name) AS "frequency count of employee last names"
FROM employees
GROUP BY last_name
ORDER BY COUNT(last_name) DESC;