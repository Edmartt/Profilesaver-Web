import click
from flask import current_app, g
from flask.cli import with_appcontext
import mariadb
from .schema import instructions
from .iconnector import IConnector


class MariaDatabase(IConnector):
    def get_db(self):
        if 'db' not in g:
            g.db = mariadb.connect(
                    host=current_app.config['MYSQL_HOST'],
                    user=current_app.config['MYSQL_USER'],
                    password=current_app.config['MYSQL_PASSWORD'],
                    database=current_app.config['MYSQL_DB']
                    )
        g.c = g.db.cursor(dictionary=True)
        return g.db, g.c

    def close_db(self, e=None):
        db_connection = g.pop('db', None)

        if db_connection is not None:
            db_connection.close()

    def init_db(self):
        db_connection, cursor = self.get_db()
        for i in instructions:
            cursor.execute(i)
        db_connection.commit()


database = MariaDatabase()


@click.command('init-db')
@with_appcontext
def init_db_command():
    database.init_db()
    click.echo('Base de datos inicializada')


def init_app(app):
    app.teardown_appcontext(database.close_db)
    app.cli.add_command(init_db_command)
