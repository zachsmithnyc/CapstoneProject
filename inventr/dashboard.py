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

@bp.route('/add_new', methods=('GET', 'POST'))
@login_required
def add_new():
    if request.method == 'POST':
        name = request.form['name']
        desc = request.form['description']
        price = request.form['price']
        qis = request.form['quantity in stock']
        reorderlevel = request.form['reorder level']
        rtd = request.form['reorder time']
        qir = request.form['quantity in reorder']
        error = None
        
        if not name:
            error = 'Name is required'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO inventory (name, desc, price, qis, reorderlevel, rtd, qir)'
                'VALUES (?, ?, ?, ?, ?, ?, ?)',
                (name, desc, price, qis, reorderlevel, rtd, qir)
            )
            db.commit()
            return redirect(url_for('dashboard'))
        
    return render_template('dash/add_new.html')
