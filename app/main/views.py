from flask import render_template, redirect, url_for, session, flash
from app.auth.views import login_required
from app.websites import Website
from . import main
from .forms import AddAccount, EditWeb


@main.route('/')
@login_required
def index():
    webs = Website.showprofiles(session['user_id'])
    return render_template('index.html', webs=webs)


@main.route('/add_account', methods=['GET', 'POST'])
@login_required
def add_account():
    form = AddAccount()
    if form.validate_on_submit():
        web = Website(form)
        web.saveweb()
        flash('Perfil Guardado correctamente')
    return render_template('add_account.html', form=form)


@main.route('/edit/<string:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    web = Website.loadWeb(id)
    form = EditWeb(username=web['web_username'], url=web['web_name'], password=web['web_pass'], notas=web['nota'], email=web['web_email'])
    return render_template('update_webs.html', web=web, form=form)


@main.route('/update/<string:id>', methods=['GET', 'POST'])
@login_required
def update(id):
    form = EditWeb()
    web = Website(form.username.data, form.url.data, form.email.data, form.password.data, form.notas.data)
    web.editWeb(id)
    flash('Datos actualizados')
    return redirect(url_for('main.index'))


@main.route('/delete/<string:id>', methods=['GET', 'POST'])
@login_required
def delete(id):
    Website.deleteWeb(id)
    flash('Dato Eliminado correctamente')
    return redirect(url_for('main.index'))


@main.route('/info', methods=['GET', 'POST'])
@login_required
def get_info():
    pass
