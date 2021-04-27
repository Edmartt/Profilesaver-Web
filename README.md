# Profilesaver-Web

Profilesaver is an application that allows to save your social media and web profiles credential
in a database.

Profilesaver can:

1. Create your user name and password for your own private space
2. Let you log in with your username and password
3. The first view is the window with your saved accounts, but the first time, the table is empty, this is the index
4. The menu option add account let you add a new account asking for username, your email, your password and a little description about the profile
5. The profilesaver password is encrypted with generate_password_hash function from Flask
6. Your session is active even if you close the browser, unless you choose to logout

# Soon:
1. Email validation format.
2. Error messages
3. Email confirmation with token
4. Username changing
5. Password changing with email confirmation message
6. Password reset option


# Running Profilesaver:

On Linux

1. python3 -m venv yourvirtualenviroment name
2. . yourvirtualenviroment/bin/activate
3. pip install -r requirements.txt
4. export FLASK_APP=app/
5. export FLASK_ENV=development
6. export FLASK_DEBUG=1
7. flask init-db
8. flask run

On Windows:

1. python3 -m venv yourvirtualenviroment name
2. . yourvirtualenviroment/bin/activate
3. pip install -r requirements.txt
4. set FLASK_APP=app/
5. set FLASK_ENV=development
6. set FLASK_DEBUG=1
7. flask init-db
8. flask run

Be sure to create a database on MySQL/MariaDB called profilesaver, anything else is created with flask init-db
