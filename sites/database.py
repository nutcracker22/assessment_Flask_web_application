import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext

DB_NAME = 'movies-data.db'


# def get_db():
#     if 'db' not in g:
#         g.db = sqlite3.connect(
#             current_app.config[DB_NAME],
#             detect_types=sqlite3.PARSE_DECLTYPES
#         )
#         g.db.row_factory = sqlite3.Row
#     return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_app(app):
    app.teardown_appcontext(close_db)
#    app.cli.add_command(init_db_command)

def connect_to_db():
    conn = sqlite3.connect(DB_NAME, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    return cur

#def init_db():
#     db = get_db()
#
#     with current_app.open_resource('movie_db.py') as f:
#         db.executescript(f.read().decode('utf8'))
#
# @click.command('init-db')
# @with_appcontext
# def init_db_command():
#     #clear the existing data and create new tables
#     init_db()
#     click.echo('Initialised the database.')

