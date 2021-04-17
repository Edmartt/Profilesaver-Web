CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(40) NOT NULL UNIQUE,
    email VARCHAR(64) NOT NULL,
    password VARCHAR(200) NOT NULL

    );

CREATE TABLE IF NOT EXISTS Websites(
    web_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    web_name VARCHAR(60) NOT NULL,
    web_email VARCHAR(64) NOT NULL,
    web_pass VARCHAR(80) NOT NULL,
    nota VARCHAR(255) DEFAULT NULL,
    web_username VARCHAR(60) NOT NULL,
    CONSTRAINT fk_user_id FOREIGN KEY(user_id) REFERENCES Users(id) ON DELETE CASCADE
    ON UPDATE CASCADE
    );


CREATE TABLE reg_users(
    username varchar(60),
    email varchar(60),
    signup_date timestamp);

CREATE TRIGGER USERS_AI AFTER INSERT ON Users 
FOR EACH ROW 
    BEGIN 
        INSERT INTO reg_users(username,email,signup_date) VALUES (new.username,new.email,datetime('now'));
    END;
