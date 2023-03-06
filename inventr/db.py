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

