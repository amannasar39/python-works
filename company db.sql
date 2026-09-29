-- sql query for creating db file
                   --  query for displaying all databases
show databases; 
                 -- sql query for displaying databases 
                 
                 -- querry for creating new database
                 
create database company;
                     -- switch to current company name

use company;

     -- querry for creating db
     
create table employee(empid int unique not null primary key,
name varchar(20),
age int,
place varchar(20),
gender enum("male","female"),
designation varchar(20),
salary int);


INSERT INTO employee(empid, name, age, place, gender, designation, salary)
VALUES
(101, 'Aman', 22, 'Thrissur', 'male', 'Developer', 35000),
(102, 'Rahul', 25, 'Kochi', 'male', 'Manager', 55000),
(103, 'Anjali', 23, 'Calicut', 'female', 'Designer', 40000),
(104, 'Sneha', 27, 'Kollam', 'female', 'HR', 45000),
(105, 'Arjun', 24, 'Kannur', 'male', 'Tester', 32000);

                       -- queryy for reading all employee attributes

SELECT * FROM employee;

                         -- querry for reading employee name,age

select name,age from employee;


-- querry for reading empid,name,salary from employee

select empid,name,salary from employee;


-- querry for employee record having place="ekm" and salary>1000
select * from employee where place="ekm" and salary>1000;

-- employee having places other than ekm
select * from employee where not(place="ekm");
select * from employee where place="ekm";


-- employee having name starts with 'A'

select * from employee where name like 'A%';

-- employee having 4 letter name ends with 'n'

select * from employee where name like '___n';

-- employees whose place ends with letter 'm'
select * from employee where place like '%m';

-- employee having 5 letter name
select * from employee where name like '_____';

-- employee having age 23 or 25
select * from employee where age in(23,25);

-- display all employee details in ascending order of salary
select * from employee order by salary asc;

-- display all employee details in descenting order of salary
select * from employee order by salary desc;

-- display unique places 
select distinct(place) from employee;
-- read first 3 rows
select * from employee limit 3;

-- read 2 rows after skipping 3 rows
select * from employee limit 2 offset 3;



