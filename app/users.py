import logging
from werkzeug.security import check_password_hash, generate_password_hash
from .database import get_db, close_db, db_connector


class User:

    id: int
    username: str
    email: str
    password: str

    def __init__(self, username: str, password: str, email=None, id=None):
        self.id = id
        self.username = username
        self.email = email
        self.password = password

    @property
    def password(self) -> None:
        raise AttributeError('Forbidden access')

    @password.setter
    def password(self, password: str) -> None:
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)

    @db_connector
    def search_username(self, username: str, **kwargs) -> dict:
        cursor = kwargs.pop('cursor')
        query = 'SELECT * FROM Users WHERE username=%s'
        cursor.execute(query, (username,))
        user = cursor.fetchone()
        if user:
            self.password_hash = user['password']
            return user

    def check_user_exists(self, username: str, email: str) -> bool:
        _, cursor = get_db()
        query = '''SELECT username, email from Users
        WHERE username=%s OR email=%s'''
        try:
            cursor.execute(query, (username, email))
            user = cursor.fetchone()
            if user:
                return True
        except:
            logging.exception('ERROR: ')
        finally:
            close_db()
        return False

    @staticmethod
    def select_user_by_id(id: int) -> dict:
        _, cursor = get_db()
        query = 'SELECT id FROM Users WHERE id=%s'
        try:
            cursor.execute(query, (id,))
            user = cursor.fetchone()
            if user:
                return user
        except:
            logging.exception('Error: ')
        finally:
            close_db()

    def register_user(self) -> None:
        connection, cursor = get_db()
        query = '''INSERT INTO users (username, email, password)
                   VALUES(%s, %s, %s)'''
        try:
            cursor.execute(query,
                           (self.username, self.email, self.password_hash))
            connection.commit()
        except:
            logging.exception('ERROR: ')
        finally:
            close_db()
