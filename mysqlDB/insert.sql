CREATE DATABASE temp_app;

USE temp_app;

CREATE TABLE temp (
    id INT NOT NULL AUTO_INCREMENT,
    weather VARCHAR(40) NOT NULL,
    time_of_day TIME NOT NULL,
    day_month DATE NOT NULL,
    PRIMARY KEY (id)
);