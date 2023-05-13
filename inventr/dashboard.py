from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from inventr.auth import login_required
from inventr.db import get_db

bp = Blueprint('dashboard', __name__)

@bp.route('/')
def dashboard():
    db = get_db()
    inventory = db.execute(
        'Select *'
        'FROM inventory'
    ).fetchall()
    return render_template('dash/dash.html', inventory=inventory)