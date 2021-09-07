import logging
from .iusersdao import IUsersdao
from app.users import User
from app.database import db_connector, get_db, close_db


class UserDao(IUsersdao):

    def get(self, user: User) -> dict:
        connection, cursor = get_db()
        query = 'SELECT * FROM Users WHERE username=%s'

        try:
            cursor.execute(query, (user.username,))
            user_data = cursor.fetchone()
            if user_data:
                user.password_hash = user_data['password']
                return user_data
        except:
            logging.exception('ERROR: ')
        finally:
            close_db()

    def add(self, user: User) -> None:
        connection, cursor = get_db()
        query = '''INSERT INTO users (username, email, password)
                   VALUES(%s, %s, %s)'''
        try:
            cursor.execute(query,
                           (user.username, user.email, user.password_hash))
            connection.commit()
        except:
            logging.exception('ERROR: ')
        finally:
            close_db()

    def check_user_exists(self, user: User) -> bool:
        _, cursor = get_db()
        query = '''SELECT username, email from Users
        WHERE username=%s OR email=%s'''
        try:
            cursor.execute(query, (user.username, user.email))
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
