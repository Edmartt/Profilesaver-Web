# Profilesaver-Web 🔐


📖 **Profilesaver** is a web application that allows to save your social media and web profiles credential in a database.

Profilesaver can:

     1. Create your username and password for your own private space
     2. Let you log in with your username and password
     3. The first view is the window with your saved accounts, but the first time, the table is empty, this is the index
     4. The menu option add account let you add a new account asking for username, your email, your password and a little description about the profile
     5. The profilesaver password is encrypted with generate_password_hash function from Flask
     6. Your session is active even if you close the browser, unless you choose to logout

## Soon 🔜
     1. Email validation format.
     2. Error messages
     3. Email confirmation with token
     4. Username changing
     5. Password changing with email confirmation message
     6. Password reset option


## 💥 Requirement

### On Linux:
     1. python3 -m venv name
     2. . name/bin/activate
     3. pip3 install -r requirements.txt
     4. create a .env file
     5. add to the .env file FLASK_APP=run.py, FLASK_ENV=development, SECRET_KEY=any value you want for test purpose only. </br>
     HOST=localhost, USER=your username, PASSWORD= your server password, DATABASE=create a new database and use that name
     12. flask init-db
     13. flask run

optionally, you can create a .sh file at the same level of the project folder with all the enviroment variable and type **. myfile.sh**

### On Windows:
     1. python -m venv name
     2. . name/Scripts/activate
     3. pip install -r requirements.txt
     4. create a .env file
     5. add to the .env file FLASK_APP=run.py, FLASK_ENV=development, SECRET_KEY=any value you want for test purpose only. </br>
     HOST=localhost, USER=your username, PASSWORD= your server password, DATABASE=create a new database and use that name
     12. flask init-db
     13. flask run

### 🔐 DEMO
If you want to test Profilesaver:
     1. Signup: you'll be asked for username, email and password
     2. You'll be redirected to the login page and now you can log in
     3. Add some accounts.
     4. Give me some advice

[Profilesaver Demo](https://shinigami.pythonanywhere.com)
