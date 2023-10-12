CREATE DATABASE IF NOT EXISTS grades_app;

USE grades_app;

CREATE TABLE grades (
    id INT NOT NULL AUTO_INCREMENT,
    course VARCHAR(25) NOT NULL,
    first_name VARCHAR(25) NOT NULL,
    last_name VARCHAR(25) NOT NULL,
    grade FLOAT NOT NULL,
    PRIMARY KEY (id)
);

GRANT ALL PRIVILEGES ON grades_app.* TO 'user'@'%';
FLUSH PRIVILEGES;
