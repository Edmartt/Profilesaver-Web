from .database import get_db,close_db,g
from flask import session
from sqlite3 import DatabaseError
class Website:
    def __init__(self,web_username,web_name,web_email,web_pass,nota,user_id=None,id=None):
        self.web_username=web_username
        self.web_name=web_name
        self.web_email=web_email
        self.web_pass=web_pass
        self.nota=nota
        self.user_id=user_id
        self.id=id

    def saveweb(self,web):
        try:
            db,cursor=get_db()
            cursor.execute('INSERT INTO Websites (user_id,web_name,web_email,web_pass,nota,web_username) VALUES(%s,%s,%s,%s,%s,%s)',(self.user_id,self.web_name,self.web_email,self.web_pass,self.nota,self.web_username))
            db.commit()
        except Exception as e:
            print(e)
        finally:
            close_db()

    @staticmethod
    def showprofiles(user_id):
        try:
            db,cursor=get_db()
            cursor.execute('SELECT * FROM Websites WHERE user_id=%s',(user_id,))
            webs=cursor.fetchall()
            return webs
        except Exception as e:
            print(e)
        finally:
            close_db()

    def editWeb(self,web_id):
        '''
        Esta función escribe los cambios en la base de datos, una vez 
        se han cargado los datos en el formulario presionando el botón edit

        :param web_id: el id del sitio web o red social guardado
        '''
        try:
            db,cursor=get_db()
            cursor.execute('UPDATE Websites SET web_name=%s,web_email=%s,web_pass=%s,nota=%s,web_username=%s WHERE web_id=%s',(self.web_name,self.web_email,self.web_pass,self.nota,self.web_username,web_id))
            db.commit()
        except Exception as e:
            print(e)

    @staticmethod
    def loadWeb(web_id):
        '''
        loadWeb carga todos los datos del sitio web seleccionado
        en el index de la aplicación  a un formulario desde donde se
        podrán editar
        :param web_id: id del sitio web o red social guardado
        '''
        try:
            db,cursor=get_db()
            cursor.execute('SELECT * FROM Websites WHERE web_id=%s',(id,))
            data=cursor.fetchone()
            return data
        except Exception as e:
            print(e)
        finally:
            close_db()

    @staticmethod
    def deleteWeb(id):
        try:
            db,cursor=get_db()
            cursor.execute('DELETE FROM Websites WHERE web_id=%s',(id,))
            db.commit()
        except Exception as e:
            print(e)
        finally:
            close_db()
