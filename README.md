# Profilesaver-Web 🔐


📖 **Profilesaver** is a web application that allows to save your social media and web profiles credential in a database.

Profilesaver can:

-    Create your username and password for your own private space
-    Let you log in with your username and password
-    The first view is the window with your saved accounts, but the first time, the table is empty, this is the index
-    The menu option add account let you add a new account asking for username, your email, your password and a little description about the profile
-    The profilesaver password is encrypted with generate_password_hash function from Flask
-    Your session is active even if you close the browser, unless you choose to logout

## Soon 🔜
-    Email validation format. ✔️
-    Error messages ✔️
-    Email confirmation with token
-    Username changing
-    Password changing with email confirmation message
-    Password reset option


## 💥Install

### On Linux:
`$ python3 -m venv name`

`$ . name/bin/activate`

`$ pip3 install -r requirements.txt`

`$ create a .env file`

     add to the .env file FLASK_APP=run.py, FLASK_ENV=development, SECRET_KEY=any value

     HOST=localhost, USER=your username, PASSWORD= your server password, DATABASE=create a new database and use that name

`$ flask init-db`

`$ flask run`

optionally, you can create a .sh file at the same level of the project folder with all the enviroment variable and type **. myfile.sh**

### On Windows:

`$ python -m venv name`

`$ . name/Scripts/activate`

`$ pip install -r requirements.txt`

`$ create a .env file`

     5. add to the .env file FLASK_APP=run.py, FLASK_ENV=development, SECRET_KEY=any value you want for test purpose only.
     HOST=localhost, USER=your username, PASSWORD= your server password, DATABASE=create a new database and use that name

`$ flask init-db`

`$ flask run`

### 🔐 DEMO
If you want to test Profilesaver:

     1. Signup: you'll be asked for username, email and password

     2. You'll be redirected to the login page and now you can log in

     3. Add some accounts.

     4. Give me some advice

[Profilesaver Demo](https://shinigami.pythonanywhere.com) Rebuilding
