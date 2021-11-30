DROP DATABASE IF EXISTS challenges;
create DATABASE challenges;
USE challenges;

DROP TABLE IF EXISTS Problem;
DROP TABLE IF EXISTS Category;

CREATE TABLE Category
(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL, 
    description VARCHAR(255)
);

CREATE TABLE Problem
(
    id INT PRIMARY KEY AUTO_INCREMENT,
    category_id INT,
    link TEXT NOT NULL, 
    FOREIGN KEY (category_id) REFERENCES Category(id)
);

