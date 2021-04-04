import functools
from flask import render_template,redirect,request,url_for,flash,session,g
from . import auth
from .forms import Login,Register
from app.users import User


@auth.before_app_request
def load_logged_in_user():
    user_id=session.get('user_id')
    if user_id is None:
        g.user=None
    else:
        g.user=User.select_user_by_id(user_id)

@auth.route('/login',methods=['GET','POST'])
def login():
    form=Login()
    if form.validate_on_submit():
        user=User.select_user(form.username.data)
        if user is not None and user.verify_password(form.password.data):
            session.clear()
            session['user_id']=user.id
            print("mi id: ",session['user_id'])
            flash('Sesion iniciada')
            return redirect(url_for('main.index'))
        else:
            flash('Nombre de usuario o contraseña no válido')
            return redirect(url_for('auth.login'))
    return render_template('auth/login.html',form=form)

@auth.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('main.index'))


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            flash('Debe iniciar sesión para ver esto')
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view

@auth.route('/register',methods=['GET','POST'])
def register():
    form=Register()
    if form.validate_on_submit():
        user=User(form.username.data,form.password.data,form.email.data)
        user.password=form.password.data
        user.registerUser(user)
        flash('Usuario Registrado')
        return redirect(url_for('auth.login'))

    return render_template('auth/register.html',form=form)

