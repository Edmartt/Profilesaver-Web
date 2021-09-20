from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, Length, Regexp, EqualTo
from flask_wtf import FlaskForm


class Login(FlaskForm):

    username = StringField('Username',
                           validators=[DataRequired(), Length(1, 64)])

    password = PasswordField('Password',
                             validators=[DataRequired(), Length(8, 64)])
    submit = SubmitField('Signup')


class Register(FlaskForm):

    username = StringField(
            'Username', validators=[DataRequired(), Length(1, 64),
                                    Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                    'Wrong username format')])

    email = StringField(
            'Email', validators=[DataRequired(), Length(1, 64), Email()])

    password = PasswordField(

            'Password', validators=[DataRequired(), Length(
                8, 64, message='Password must be 8 characters minimum'),
                EqualTo('passconfirm', message='Password must match')])

    passconfirm = PasswordField(
            'Confirm Password', validators=[DataRequired()])

    submit = SubmitField('Signup')
