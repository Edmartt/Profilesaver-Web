from mariadb import ProgrammingError
from app.iconnector import IConnector


class QueryManager:

    def __init__(self, db_connector: IConnector):
        self.db_connector = db_connector

    def select(self, query, *args, all=False):
        _, cursor = self.db_connector.get_db()
        try:
            cursor.execute(query, *args)
            if all:
                return cursor.fetchall()
            else:
                return cursor.fetchone()
        except ProgrammingError as ex:
            print(ex)
        finally:
            self.db_connector.close_db()

    def insert(self, query, *args):
        connection, cursor = self.db_connector.get_db()
        try:
            cursor.execute(query, (*args))
            connection.commit()
        except ProgrammingError as ex:
            print(ex)
        finally:
            self.db_connector.close_db()
