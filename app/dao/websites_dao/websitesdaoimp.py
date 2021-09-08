from app.querymanager import QueryManager
from .iwebsitesdao import IWebsitesdao
from app.websites import Website
from app.database import get_db, close_db


class Websitedao(IWebsitesdao):

    def get(self, web_id: int, db: QueryManager) -> dict:
        query = 'SELECT * FROM Websites WHERE web_id=%s'
        data = db.select(query, web_id)
        if data:
            return data

    def get_all(self, user_id: int, db: QueryManager) -> dict:
        query = 'SELECT * FROM websites WHERE user_id=%s'
        webs = db.select(query, (user_id,), all=True)
        if webs:
            return webs
        return []

    def add(self, web: Website, db: QueryManager) -> None:
        query = '''INSERT INTO Websites(user_id, web_name, web_email, web_pass,
        nota, web_username) VALUES(%s, %s, %s, %s, %s, %s)'''

        db.insert(query, (web.user_id, web.web_name,
                          web.web_email, web.web_pass,
                          web.nota, web.web_username))

    def update(self, web: Website, web_id: int) -> None:
        connection, cursor = get_db()
        query = '''UPDATE Websites SET web_name = %s, web_email = %s,
        web_pass = %s, nota = %s, web_username = %s WHERE web_id = %s'''

        try:
            cursor.execute(query, (web.web_name, web.web_email,
                                   web.web_pass, web.nota,
                                   web.web_username, web_id))
            connection.commit()
        except Exception as ex:
            print(ex)
        finally:
            close_db()

    def delete(self, web_id):
        connection, cursor = get_db()
        query = 'DELETE FROM Websites WHERE web_id=%s'

        try:
            cursor.execute(query, (web_id,))
            connection.commit()
        except Exception as ex:
            print(ex)
        finally:
            close_db()
