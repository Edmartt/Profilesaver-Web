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
        query = '''INSERT INTO Websites(user_id, web_name, web_email, web_pass,
        nota, web_username) VALUES(%s, %s, %s, %s, %s, %s)'''
        db_connection, cursor = get_db()

        try:
            cursor.execute(query, (self.user_id, self.web_name,
                                   self.web_email, self.web_pass,
                                   self.nota, self.web_username))
            db_connection.commit()
        except Exception as e:
            print(e)
        finally:
            close_db()

    @staticmethod
    def showprofiles(user_id):
        _, cursor = get_db()
        query = 'SELECT * FROM Websites WHERE user_id=%s'

        try:
            cursor.execute(query, (user_id,))
            webs = cursor.fetchall()
            return webs
        except Exception as e:
            print(e)
        finally:
            close_db()

    def editWeb(self, web_id):
        '''
        Esta función escribe los cambios en la base de datos, una vez
        se han cargado los datos en el formulario presionando el botón edit

        :param web_id: el id del sitio web o red social guardado
        '''
        db_connection, cursor = get_db()
        query = '''UPDATE Websites SET web_name = %s, web_email = %s,
        web_pass = %s, nota = %s, web_username = %s WHERE web_id = %s'''

        try:
            cursor.execute(query, (self.web_name, self.web_email,
                                   self.web_pass, self.nota,
                                   self.web_username, web_id))
            db_connection.commit()
        except Exception as ex:
            print(ex)

    @staticmethod
    def loadWeb(web_id):
        '''
        loadWeb carga todos los datos del sitio web seleccionado
        en el index de la aplicación  a un formulario desde donde se
        podrán editar
        :param web_id: id del sitio web o red social guardado
        '''
        try:
            db_connection, cursor = get_db()
            cursor.execute('SELECT * FROM Websites WHERE web_id=%s', (id,))
            data = cursor.fetchone()
            return data
        except Exception as e:
            print(e)
        finally:
            close_db()

    @staticmethod
    def deleteWeb(id):
        db_connection, cursor = get_db()
        query = 'DELETE FROM Websites WHERE web_id=%s'

        try:
            cursor.execute(query, (id,))
            db_connection.commit()
        except Exception as ex:
            print(ex)
        finally:
            close_db()
