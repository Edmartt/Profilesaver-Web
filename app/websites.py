from flask import session
from .main.forms import AddAccount


class Website:
    __web_name: str
    __web_email: str
    __web_pass: str
    __nota: str
    __web_username: str

    web_form: AddAccount

    def __init__(self, web_form: AddAccount):
        self.__web_name = web_form.url.data
        self.__web_email = web_form.email.data
        self.__web_pass = web_form.password.data
        self.__nota = web_form.notas.data
        self.__web_username = web_form.username.data
        self.__user_id = session['user_id']

    @property
    def user_id(self):
        return self.__user_id

    @property
    def web_name(self):
        return self.__web_name

    @web_name.setter
    def web_name(self, web_name):
        self.__web_name = web_name

    @property
    def web_email(self):
        return self.__web_email

    @web_email.setter
    def web_email(self, web_email):
        self.__web_email = web_email

    @property
    def web_pass(self):
        return self.__web_pass

    @web_pass.setter
    def web_pass(self, web_pass):
        self.__web_pass = web_pass

    @property
    def nota(self):
        return self.__nota

    @nota.setter
    def nota(self, nota):
        self.__nota = nota

    @property
    def web_username(self):
        return self.__web_username

    @web_username.setter
    def web_username(self, web_username):
        self.__web_username = web_username
