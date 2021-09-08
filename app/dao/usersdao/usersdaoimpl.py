from app.querymanager import QueryManager
from .iusersdao import IUsersdao
from app.users import User


class UserDao(IUsersdao):

    def get(self, user: User, db: QueryManager) -> dict:
        query = 'SELECT * FROM users WHERE username=?'
        user_data = db.select(query, (user.username,), all=False)
        if user_data:
            user.password_hash = user_data['password']
            return user_data

    def add(self, user: User, db: QueryManager) -> None:
        query = '''INSERT INTO users (username, email, password)
                   VALUES(%s, %s, %s)'''
        db.insert(query,
                  (user.username, user.email, user.password_hash))

    def check_user_exists(self, user: User, db: QueryManager) -> bool:
        query = '''SELECT username, email from Users
        WHERE username=%s OR email=%s'''
        user = db.select(query, (user.username, user.email), all=False)
        if user:
            return True
        return False

    @staticmethod
    def select_user_by_id(id: int, db: QueryManager) -> dict:
        query = 'SELECT id FROM Users WHERE id=%s'
        user = db.select(query, (id,), all=False)
        if user:
            return user
