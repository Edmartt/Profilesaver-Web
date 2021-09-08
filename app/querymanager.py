from mariadb import ProgrammingError
from app.database import get_db, close_db


class QueryManager:

    def select(self, query, *args, all=False):
        _, cursor = get_db()
        try:
            cursor.execute(query, *args)
            if all:
                return cursor.fetchall()
            else:
                return cursor.fetchone()
        except ProgrammingError as ex:
            print(ex)
        finally:
            close_db()

    def insert(self, query, *args):
        connection, cursor = get_db()
        try:
            cursor.execute(query, (*args))
            connection.commit()
        except ProgrammingError as ex:
            print(ex)
        finally:
            close_db()
