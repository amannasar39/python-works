CREATE DATABASE company1;

USE company1;

CREATE TABLE departments (
    id INT NOT NULL PRIMARY KEY,
    department_name VARCHAR(20)
);

CREATE TABLE employee (
    id INT NOT NULL PRIMARY KEY,
    employee_name VARCHAR(50),
    age INT,
    salary INT,
    joining_year INT,
    department_id INT,
    city VARCHAR(50),
    FOREIGN KEY (department_id) REFERENCES departments(id)
);

INSERT INTO departments (id, department_name)
VALUES
(1, "sales"),
(2, "it"),
(3, "hr");

SELECT * FROM departments;

INSERT INTO employee
(id, employee_name, age, salary, joining_year, department_id, city)
VALUES
(1, "Aman", 22, 50000, 2022, 2, "Kochi"),
(2, "Arun", 25, 65000, 2021, 1, "Kochi"),
(3, "Anjali", 24, 45000, 2020, 3, "Thrissur"),
(4, "Ramesh", 28, 70000, 2023, 2, "Kochi"),
(5, "Rahul", 26, 55000, 2019, 1, "Calicut"),
(6, "Anu", 23, 48000, 2022, 3, "Thrissur");

select * from employee;

-- retrive all record from dept table
select * from departments;

-- retrive employee name age salary from employee table
select employee_name,salary,age from employee;
-- Display the employees whose salary is greater than 50,000.
select employee_name,salary from employee where salary > 50000;
-- Display the employees whose name starts with the letter "A"
select employee_name,salary,age from employee where employee_name like 'A%';
-- Display the employees who joined after 2020 and earn more than 60,000
select employee_name,salary,age from employee where joining_year > 2020 and salary > 60000;
-- Display the employees from Kochi, sorted by salary in descending order
select employee_name,salary,age from employee where city = "kochi" order by salary desc;
-- Display the number of employees in each department
select department_id,count(*) from employee group by department_id;
-- Display the average salary for each city
select city,avg(salary) from employee group by city;
-- Display the cities where the average salary is greater than 45,000
select city,avg(salary) from employee group by city having avg(salary) > 45000;
-- Display the employee name along with the corresponding department name
select employee.employee_name,departments.department_name from employee inner join departments on employee.department_id = departments.id;
