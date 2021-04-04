from flask_wtf import FlaskForm
from wtforms.validators import DataRequired,Length,Email,EqualTo,Regexp
from wtforms import StringField,PasswordField,TextAreaField,SubmitField
from wtforms import ValidationError

class AddAccount(FlaskForm):
    username=StringField('Username',validators=[DataRequired()])
    url=StringField('URL DEL SITIO',validators=[DataRequired(),Length(1,64)])
    email=StringField('Email',validators=[DataRequired()])
    password=PasswordField('Password',validators=[DataRequired(),EqualTo('passconfirm',message='El password no coincide'),Length(8,64)])
    passconfirm=PasswordField('Confirmar Password',validators=[DataRequired(),Length(8,64)])
    notas=TextAreaField('Anotaciones sobre este perfil',validators=[DataRequired()])
    submit=SubmitField('Guardar')

class EditWeb(FlaskForm):
    username=StringField('Username',validators=[DataRequired()])
    url=StringField('URL DEL SITIO',validators=[DataRequired(),Length(1,64)])
    email=StringField('Email',validators=[DataRequired()])
    password=StringField('Password',validators=[DataRequired()])
    notas=TextAreaField('Anotaciones sobre este perfil',validators=[DataRequired()])
    submit=SubmitField('Modificar')

