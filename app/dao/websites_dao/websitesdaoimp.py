from .iwebsitesdao import IWebsitesdao
from app.websites import Website
from app.database import get_db, close_db


class Websitedao(IWebsitesdao):

    def get(self, web_id: int) -> dict:
        _, cursor = get_db()
        try:
            cursor.execute('SELECT * FROM Websites WHERE web_id=%s', (web_id,))
            data = cursor.fetchone()
            if data:
                return data
        except Exception as ex:
            print(ex)
        finally:
            close_db()

    def get_all(self, user_id: int) -> dict:
        _, cursor = get_db()
        query = 'SELECT * FROM websites WHERE user_id=%s'
        try:
            cursor.execute(query, (user_id,))
            webs = cursor.fetchall()
            return webs
        except Exception as ex:
            print(ex)
        finally:
            close_db()

    def add(self, web: Website) -> None:
        connection, cursor = get_db()
        query = '''INSERT INTO Websites(user_id, web_name, web_email, web_pass,
        nota, web_username) VALUES(%s, %s, %s, %s, %s, %s)'''

        try:
            cursor.execute(query, (web.user_id, web.web_name,
                                   web.web_email, web.web_pass,
                                   web.nota, web.web_username))
            connection.commit()
        except Exception as ex:
            print(ex)
        finally:
            close_db()

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
