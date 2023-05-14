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
        qis = request.form['quantity']
        reorderlevel = request.form['reorder_level']
        rtd = request.form['reorder_time']
        qir = request.form['quantity_in_reorder']
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
            message = 'Item added successfully'
            flash(message)
            return redirect(url_for('dashboard'))
        
    return render_template('dash/add_new.html')

def get_item(id):
    item = get_db().execute(
        'SELECT *'
        ' FROM inventory'
        ' WHERE id = ?',
        (id,)
    ).fetchone()

    if item is None:
        abort(404, f"Item {id} doesn't exist.")

    return item

@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    item = get_item(id)

    if request.method == 'POST':
        name = request.form['name']
        desc = request.form['description']
        price = request.form['price']
        qis = request.form['quantity']
        reorderlevel = request.form['reorder_level']
        rtd = request.form['reorder_time']
        qir = request.form['quantity_in_reorder']
        discont = request.form['discontinued']
        error = None

        if not name:
            error = 'name is required'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE inventory SET name = ?, desc = ?, price = ?, qis = ?, reorderlevel = ?, rtd = ?, qir = ?, discont = ?'
                'WHERE id = ?',
                (name, desc, price, qis, reorderlevel, rtd, qir, discont)
            )
            db.commit()
            return redirect(url_for('dashboard'))
    return render_template('dash/update.html', item=item)

@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    get_item(id)
    db = get_db()
    db.execute('DELETE FROM inventory WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('dashboard'))
