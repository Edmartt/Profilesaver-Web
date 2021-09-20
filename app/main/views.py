from flask import render_template, redirect, url_for, flash
from app.querymanager import QueryManager
from app.database import MariaDatabase
from app.auth.views import login_required
from app.dao.websites_dao.iwebsitesdao import IWebsitesdao
from app.dao.websites_dao.websitesdaoimp import Websitedao
from app.websites import Website
from . import main
from .forms import AddAccount, EditWeb


@main.route('/')
@login_required
def index():
    websitedao: IWebsitesdao
    form = AddAccount()
    website = Website(form)
    websitedao = Websitedao()
    db_manager = QueryManager(MariaDatabase())
    webs = websitedao.get_all(website.user_id, db_manager)
    return render_template('index.html', webs=webs)


@main.route('/add_account', methods=['GET', 'POST'])
@login_required
def add_account():
    form = AddAccount()
    db_manager = QueryManager(MariaDatabase())
    websitedao: IWebsitesdao

    if form.validate_on_submit():
        website = Website(form)
        websitedao = Websitedao()
        websitedao.add(website, db_manager)
        flash('Perfil Guardado correctamente')
    return render_template('add_account.html', form=form)


@main.route('/edit/<string:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    websitedao: IWebsitesdao
    db_manager = QueryManager(MariaDatabase())
    websitedao = Websitedao()
    web = websitedao.get(id, db_manager)
    form = EditWeb(username=web['web_username'], url=web['web_name'], password=web['web_pass'], notas=web['nota'], email=web['web_email'])
    return render_template('update_webs.html', web=web, form=form)


@main.route('/update/<string:id>', methods=['GET', 'POST'])
@login_required
def update(id):
    web_form = EditWeb()
    website = Website(web_form)
    websitedao: IWebsitesdao
    websitedao = Websitedao()
    websitedao.update(website, id)
    flash('Datos actualizados')
    return redirect(url_for('main.index'))


@main.route('/delete/<string:id>', methods=['GET', 'POST'])
@login_required
def delete(id):
    websitedao: IWebsitesdao
    websitedao = Websitedao()
    websitedao.delete(id)
    flash('Dato Eliminado correctamente')
    return redirect(url_for('main.index'))
