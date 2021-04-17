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
            cursor=get_db()
            cursor.execute('INSERT INTO Websites (user_id,web_name,web_email,web_pass,nota,web_username) VALUES(?,?,?,?,?,?)',(session['user_id'],self.web_name,self.web_email,self.web_pass,self.nota,self.web_username))
            cursor.commit()
        except Exception as e:
            print(e)
        finally:
            close_db()

    @staticmethod
    def showprofiles(user_id):
        try:
            cursor=get_db().cursor()
            cursor.execute('SELECT * FROM Websites WHERE user_id=?',(user_id,))
            webs=cursor.fetchall()
            return webs
        except Exception as e:
            print(e)
        finally:
            close_db()

    def editWeb(self,web_id):
        try:
            close_db()
            cursor=get_db()
            cursor.execute('UPDATE Websites SET web_name=?,web_email=?,web_pass=?,nota=?,web_username=? WHERE web_id=?',(self.web_name,self.web_email,self.web_pass,self.nota,self.web_username,web_id))
            cursor.commit()
        except Exception as e:
            print(e)

    @staticmethod
    def loadWeb(id):
        try:
            cursor=get_db().cursor()
            cursor.execute('SELECT * FROM Websites WHERE web_id=?',(id,))
            data=cursor.fetchone()
            return data
        except Exception as e:
            print(e)
        finally:
            close_db()

    @staticmethod
    def deleteWeb(id):
        try:
            close_db()
            cursor=get_db()
            cursor.execute('DELETE FROM Websites WHERE web_id=?',(id,))
            cursor.commit()
        except Exception as e:
            print(e)
        finally:
            close_db()
