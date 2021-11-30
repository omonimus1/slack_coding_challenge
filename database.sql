DROP DATABASE IF EXISTS challenges;
create DATABASE challenges;
USE challenges;

DROP TABLE IF EXISTS Problem;
DROP TABLE IF EXISTS Category;

CREATE TABLE Category
(
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL, 
    description VARCHAR(255) DEFAULT NULL
);

INSERT INTO Category(name, description) Values('data-structure', 'Algorithms and DataStuctures coding challenges');
INSERT INTO Category(name) Values('machine-learning');
INSERT INTO Category(name) Values('behavioural');
INSERT INTO Category(name) Values('system-design');


CREATE TABLE Problem
(
    id INT PRIMARY KEY AUTO_INCREMENT,
    category_id INT,
    link TEXT NOT NULL, 
    FOREIGN KEY (category_id) REFERENCES Category(id)
);

