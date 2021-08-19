from werkzeug.security import check_password_hash,generate_password_hash
from .database import get_db, close_db

class User:

    def __init__(self, username, password, email=None, id=None):
        self.id = id
        self.username = username
        self.email = email
        self.password = password

    @property
    def password(self):
        raise AttributeError('No tiene acceso a esta propiedad')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


    def select_user(self, username):
        try:
            db, cursor = get_db()
            cursor.execute('SELECT * FROM Users WHERE username=%s', (username,))
            user = cursor.fetchone()

            if user:
                return user
        except Exception as e:
            print(e)
        finally:
            close_db()

    @staticmethod
    def select_user_by_id(id):
        try:
            db, cursor = get_db()
            cursor.execute('SELECT * FROM Users WHERE id=%s', (id,))
            user = cursor.fetchone()
            if user:
                return user
        except Exception as e:
            print(e)
        finally:
            close_db()

    def registerUser(self, user):
        try:
            db, cursor = get_db()
            cursor.execute('INSERT INTO Users (username,email,password) VALUES(%s,%s,%s)', (self.username, self.email, self.password_hash))
            db.commit()
        except Exception as e:
            print(e)
        finally:
            close_db()
