instructions=[
    'SET FOREIGN_KEY_CHECKS=0;',
    'DROP TABLE IF EXISTS Users;',
    'DROP TABLE IF EXISTS Websites;',
    'DROP TABLE IF EXISTS reg_users;',
    'SET FOREIGN_KEY_CHECKS=1;',

    """CREATE TABLE IF NOT EXISTS Users(
    id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(40) NOT NULL UNIQUE,
    email VARCHAR(64) NOT NULL,
    password VARCHAR(150) NOT NULL
    );""",

    """CREATE TABLE IF NOT EXISTS Websites(
    web_id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    user_id INT UNSIGNED NOT NULL,
    web_name VARCHAR(60) NOT NULL,
    web_email VARCHAR(64) NOT NULL,
    web_pass VARCHAR(80) NOT NULL,
    nota VARCHAR(255),
    web_username VARCHAR(60) NOT NULL,
    CONSTRAINT FK_user_id FOREIGN KEY (user_id) REFERENCES Users(id) ON DELETE CASCADE
    ON UPDATE CASCADE);
    """,

    """CREATE TABLE reg_users(
    username varchar(60),
    email varchar(60),
    signup_date timestamp);
    """,

    """
    CREATE TRIGGER USERS_AI AFTER INSERT ON Users
    FOR EACH ROW
    BEGIN
        INSERT INTO reg_users(username,email,signup_date) VALUES (new.username,new.email,now());
    END;

    """
]
