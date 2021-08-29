from flask import session
from .main.forms import AddAccount
from .database import get_db, close_db


class Website:
    def __init__(self, web_form):
        web_form = AddAccount()
        self.web_username = web_form.username.data
        self.web_name = web_form.url.data
        self.web_email = web_form.email.data
        self.web_pass = web_form.password.data
        self.nota = web_form.email.data
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

    def showprofiles(self):
        _, cursor = get_db()
        query = 'SELECT * FROM Websites WHERE user_id=%s'
        try:
            cursor.execute(query, (self.user_id,))
            webs = cursor.fetchall()
            if webs:
                return webs
        except Exception as ex:
            print(ex)
        finally:
            pass

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

    @staticmethod
    def deleteWeb(id):
        connection, cursor = get_db()
        query = 'DELETE FROM Websites WHERE web_id=%s'
        try:
            cursor.execute(query, (id,))
            connection.commit()
        except Exception as ex:
            print(ex)
