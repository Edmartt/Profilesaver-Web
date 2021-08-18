import functools
from flask import render_template, redirect,\
        request, url_for, flash, session, g

from app.users import User
from . import auth
from .forms import Login, Register


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            flash('Debe iniciar sesión para ver esto')
            # redirigiremos a login en cada intento de acceder a una vista
            # la variable next, guarda la url que se quiso visitar
            return redirect(url_for('auth.login', next=request.url_rule))
        return view(**kwargs)
    return wrapped_view


@auth.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    g.user = None if user_id is None else User.select_user_by_id(user_id)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = Login()

    if form.validate_on_submit():
        user = User(form.username.data, form.password.data)
        user_data = user.select_user(form.username.data)

        if user_data is not None and user.verify_password(form.password.data):
            session.clear()
            session['user_id'] = user_data['id']
            next = request.args.get('next', None)

            if next is None or not next.startswith('/'):
                next = url_for('main.index')
            return redirect(next)

        flash('Nombre de usuario o contraseña no válido')
    return render_template('auth/login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    session.clear()
    return redirect(url_for('main.index'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = Register()

    if session.get('user_id') is not None:
        return redirect(url_for('main.index'))

    else:
        if form.validate_on_submit():
            user = User(form.username.data,
                        form.email.data, form.password.data)
            user.password = form.password.data
            user.registerUser(user)
            flash('Usuario Registrado')
            return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)
