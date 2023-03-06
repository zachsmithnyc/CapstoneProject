import sqlite3 as lite
import click 
from flask import current_app, g

def get_db():
    if 'db' not in g:
        g.db = lite.connect(
            current_app.config['DATABASE'],
            detect_types=lite.PARSE_DECLTYPES
        )
        g.db.row_factory = lite.Row

    return g.db

def close_db(e=None):
    db=g.pop('db', None)

    if db is not None:
        db.close()

def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

@click.command('init-db')
def init_db_command():
    # command to clear the existing data and create new tables
    init_db()
    click.echo('Initialized the database.')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
    