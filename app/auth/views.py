import functools
from flask import render_template, redirect,\
        request, url_for, flash, session, g
from app.iconnector import IConnector
from app.database import MariaDatabase

from app.users import User
from app.querymanager import QueryManager
from app.dao.usersdao.iusersdao import IUsersdao
from app.dao.usersdao.usersdaoimpl import UserDao
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
    db_manager = QueryManager(MariaDatabase())
    g.user = None if user_id is None else UserDao.select_user_by_id(
            user_id, db_manager)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = Login()
    db_manager: QueryManager
    userdao: IUsersdao  # acceso a los metodos implementados de la interfaz
    user: User

    if session.get('user_id', None) is not None:
        return redirect(url_for('main.index'))

    elif form.validate_on_submit():
        user = User(form.username.data, form.password.data)
        userdao = UserDao()
        db_manager = QueryManager(MariaDatabase())
        user_data = userdao.get(user, db_manager)

        if user_data is not None and user.verify_password(
                form.password.data):
            session.clear()
            session['user_id'] = user_data['id']
            next = request.args.get('next', None)

            if next is None or not next.startswith('/'):
                next = url_for('main.index')
            return redirect(next)
        flash('Wrong username or password')
    return render_template('auth/login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    session.clear()
    return redirect(url_for('main.index'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    userdao: IUsersdao
    userdao = UserDao()
    db_manager = QueryManager(MariaDatabase())
    user: User
    form = Register()

    if session.get('user_id', None) is not None:
        return redirect(url_for('main.index'))

    elif form.validate_on_submit():
        user = User(form.username.data,
                    form.password.data, form.email.data)

        if userdao.check_user_exists(user, db_manager):
            flash('An user with this email or username already exists')
        else:
            userdao.add(user, db_manager)
            flash('User registered')
            return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)
