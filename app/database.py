import click
from flask import current_app, g
from flask.cli import with_appcontext
import mariadb
from .schema import instructions


def get_db():
    if 'db' not in g:
        g.db = mariadb.connect(
            host=current_app.config['MYSQL_HOST'],
            user=current_app.config['MYSQL_USER'],
            password=current_app.config['MYSQL_PASSWORD'],
            database=current_app.config['MYSQL_DB']
        )
        g.c = g.db.cursor(dictionary=True)
        return g.db, g.c


def db_connector(func):  # decorator that makes connection to db
    def wrapper(*args, **kwargs):
        connection, cursor = get_db()
        try:
            result = func(*args, cursor=cursor, **kwargs)
        except:
            connection.rollback()
            raise
        else:
            connection.commit()
        finally:
            connection.close()
        return result
    return wrapper


def close_db(e=None):
    db_connection = g.pop('db', None)

    if db_connection is not None:
        db_connection.close()


def init_db():
    db_connection, cursor = get_db()
    for i in instructions:
        cursor.execute(i)
    db_connection.commit()


@click.command('init-db')
@with_appcontext
def init_db_command():
    init_db()
    click.echo('Base de datos inicializada')


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
