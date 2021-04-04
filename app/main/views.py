from flask import render_template,redirect,url_for,session,g,request,flash
from . import main
from .forms import AddAccount,EditWeb
from app.websites import Website
from app.auth.views import login_required
from ..database import get_db,close_db

@main.route('/')
@login_required
def index():
    webs=Website.showprofiles(session['user_id'])
    return render_template('index.html',webs=webs)


@main.route('/add_account',methods=['GET','POST'])
@login_required
def add_account():
    form=AddAccount()
    try:
        if form.validate_on_submit():
            web=Website(form.username.data,form.url.data,form.email.data,form.password.data,form.notas.data,session['user_id'])
            web.saveweb(web)
            flash('Perfil Guardado correctamente')
    except Exception as e:
        print(e)
    return render_template('add_account.html',form=form)


@main.route('/edit/<string:id>',methods=['GET','POST'])
@login_required
def edit(id):
    web=Website.loadWeb(id)
    form=EditWeb(username=web[6],url=web[2],password=web[4],notas=web[5],email=web[3])
    return render_template('update_webs.html',web=web,form=form)

@main.route('/update/<string:id>',methods=['GET','POST'])
@login_required
def update(id):
    form=EditWeb()
    web=Website(form.username.data,form.url.data,form.email.data,form.password.data,form.notas.data)
    web.editWeb(id)
    flash('Datos actualizados')
    return redirect(url_for('main.index'))

@main.route('/delete/<string:id>',methods=['GET','POST'])
def delete(id):
    Website.deleteWeb(id)
    flash('Dato Eliminado correctamente')
    return redirect(url_for('main.index'))
