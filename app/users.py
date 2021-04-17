from werkzeug.security import check_password_hash,generate_password_hash
from .database import get_db,close_db

class User:

    def __init__(self,username,password,email=None,id=None):
        self.id=id
        self.username=username
        self.email=email
        self.password_hash=password

    @property
    def password(self):
        raise AttributeError ('No tiene acceso a esta propiedad')

    @password.setter
    def password(self,password):
        self.password_hash=generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    @staticmethod
    def select_user(username):
        try:

            cursor=get_db().cursor()
            cursor.execute('SELECT * FROM Users WHERE username=?',(username,))
            user=cursor.fetchone()
            if user:
                id=user[0]
                username=user[1]
                email=user[2]
                password=user[3]
                return User(username,password,email,id)
        except Exception as e:
            print(e)
        finally:
            close_db()

    @staticmethod
    def select_user_by_id(id):
        try:
            cursor=get_db().cursor()
            cursor.execute('SELECT * FROM users WHERE id=?',(id,))
            user=cursor.fetchone()
            if user:
                return user
        except Exception as e:
            print(e)
        finally:
            close_db()

    def registerUser(self,user):
        #close_db()
        try:
            cursor=get_db()
            cursor.execute('INSERT INTO Users (username,password,email) VALUES(?,?,?)',(self.username,self.password_hash,self.email))
            cursor.commit()
        except Exception as e:
            print(e)
        finally:
            close_db()

