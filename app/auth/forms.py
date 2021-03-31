from wtforms import StringField,SubmitField,PasswordField
from wtforms.validators import DataRequired,Email,Length,Regexp,EqualTo
from flask_wtf import FlaskForm


class Login(FlaskForm):
    username=StringField('Username',validators=[DataRequired(),Length(1,64)])
    password=PasswordField('Password',validators=[DataRequired()])
    submit=SubmitField('Iniciar')

class Register(FlaskForm):
    username=StringField('Username',validators=[DataRequired(),Length(1,64),Regexp('^[A-Za-z][A-Za-z0-9_.]*$',0,'El nombre de usuario no debe contener caracteres extraños')])
    email=StringField('Email',validators=[DataRequired(),Length(1,64)])
    password=PasswordField('Password',validators=[DataRequired()])
    submit=SubmitField('Registrarse')
