CREATE DATABASE task_db;

USE task_db;

CREATE TABLE users (
    id INT NOT NULL PRIMARY KEY,
    name VARCHAR(20) NOT NULL UNIQUE,
    email VARCHAR(30) NOT NULL UNIQUE,
    phone VARCHAR(20) NOT NULL
);

CREATE TABLE Task (
    id INT NOT NULL PRIMARY KEY,
    title VARCHAR(20),
    user_id INT,
    status ENUM('pending', 'finished') DEFAULT 'pending',
    date DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);


INSERT INTO users (id, name, email, phone)
VALUES
(1, 'aman', 'aman123@gmail.com', '34567890'),
(2, 'arun', 'arun987@gmail.com', '44654153163'),
(3, 'edwin', 'edwin5456@gmail.com', '6546546554');



INSERT INTO Task (id, title, user_id)
VALUES
(1, 'Learn Python', 1),
(2, 'Complete SQL', 1),
(3, 'Build Website', 2),
(4, 'Learn Django', 2),
(5, 'Create Project', 3);

use task_db;

select * from users;

select * from task;

select * from users inner join task on user_id=task.user_id;

select name,title,status from users left join task on users.id=task.user_id;

select name,title,status from users cross join users.id=task.user_id;

SELECT 
    users.name,
    Task.title,
    Task.status
FROM users
CROSS JOIN Task;



