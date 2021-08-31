from flask import session
from .database import get_db, close_db


class Website:
    def __init__(self, web_form):
        self.web_username = web_form.username.data
        self.web_name = web_form.url.data
        self.web_email = web_form.email.data
        self.web_pass = web_form.password.data
        self.nota = web_form.notas.data
        self.user_id = session['user_id']

    def saveweb(self):
        connection, cursor = get_db()
        query = '''INSERT INTO Websites(user_id, web_name, web_email, web_pass,
        nota, web_username) VALUES(%s, %s, %s, %s, %s, %s)'''

        try:
            cursor.execute(query, (self.user_id, self.web_name,
                                   self.web_email, self.web_pass,
                                   self.nota, self.web_username))
            connection.commit()
        except Exception as ex:
            print(ex)
        finally:
            close_db()

    def showprofiles(self):
        _, cursor = get_db()
        query = 'SELECT * FROM websites WHERE user_id=%s'
        try:
            cursor.execute(query, (self.user_id,))
            webs = cursor.fetchall()
            return webs
        except Exception as ex:
            print(ex)
        finally:
            close_db()

    def editWeb(self, web_id):
        connection, cursor = get_db()
        query = '''UPDATE Websites SET web_name = %s, web_email = %s,
        web_pass = %s, nota = %s, web_username = %s WHERE web_id = %s'''

        try:
            cursor.execute(query, (self.web_name, self.web_email,
                                   self.web_pass, self.nota,
                                   self.web_username, web_id))
            connection.commit()
        except Exception as ex:
            print(ex)
        finally:
            close_db()

    @staticmethod
    def loadWeb(web_id):
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

    @staticmethod
    def deleteWeb(id):
        connection, cursor = get_db()
        query = 'DELETE FROM Websites WHERE web_id=%s'
        try:
            cursor.execute(query, (id,))
            connection.commit()
        except Exception as ex:
            print(ex)
        finally:
            close_db()
