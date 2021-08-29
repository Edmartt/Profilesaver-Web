import logging
from werkzeug.security import check_password_hash, generate_password_hash
from .database import get_db, close_db, db_connector


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

    @db_connector
    def select_user(self, username, **kwargs):
        cursor = kwargs.pop('cursor')
        query = 'SELECT * FROM Users WHERE username=%s'
        cursor.execute(query, (username,))
        user = cursor.fetchone()
        if user:
            return user

    @staticmethod
    def select_user_by_id(id):
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

    def registerUser(self, user):
            connection, cursor = get_db()
            query = '''INSERT INTO Users (username, email, password)
            VALUES(%s, %s, %s)'''
            try:
                cursor.execute(query, (
                    self.username, self.email, self.password_hash))
                connection.commit()
            except:
                logging.exception("Error: ")
