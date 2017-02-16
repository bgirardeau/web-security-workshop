# -*- coding: utf-8 -*-
"""
A simple web application to view and publish notes.
"""
import os

from flask import (
    request, session, g, redirect, url_for, abort,
    render_template, flash
)
from flask_login import (
    LoginManager, current_user, login_user, login_required,
    logout_user
)

from ._app import app
from .db import db, text, escape_string, User, Note


login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user_from_id(user_id):
    user = User.query.filter_by(id=int(user_id)).first()
    return user


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if not user or not user.check_password(request.form['password']):
            error = 'Invalid username or password'
        else:
            login_user(user)
            flash('You were logged in')
            return redirect(url_for('show_notes'))
    return render_template('login.html', error=error)


@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        exist_user = User.query.filter_by(
            username=request.form['username']
        ).first()
        if exist_user:
            error = 'Username is already in use'
        else:
            user = User(username=request.form['username'],
                        password=request.form['password'],
                        first_name=request.form.get('first_name', ''),
                        last_name=request.form.get('last_name', ''))
            db.session.add(user)
            db.session.commit()
            flash('You have been registered')
            return redirect(url_for('login'))
    return render_template('register.html', error=error)


@app.route('/')
def show_notes():
    notes = db.session.execute(
        text("select notes.id, notes.public, notes.author, notes.title, "
             "notes.text, users.username "
             "from notes inner join users on notes.author=users.id "
             "order by notes.date_created asc")
    )
    return render_template('show_notes.html', notes=notes)


@app.route('/add', methods=['POST'])
@login_required
def add_note():
    user_id = current_user.id
    title = escape_string(request.form.get('title', ''))
    note_text = escape_string(request.form.get('text', ''))
    public = 1 if request.form.get('public', '') == 'on' else 0

    db.session.execute(
        text(u'insert into notes (public, author, title, text) values (%s, %s, "%s", "%s")' %
             (public, user_id, title, note_text))
    )
    db.session.commit()

    flash('Note posted')
    return redirect(url_for('show_notes'))


@app.route('/remove', methods=['POST'])
@login_required
def remove_note():
    user_id = current_user.id
    id = request.form['id']
    if not id:
        return redirect(url_for('show_notes'))

    db.session.execute(
        text('delete from notes where id=%s and author=%s ' % (id, user_id))
    )
    db.session.commit()

    flash('Note deleted')
    return redirect(url_for('show_notes'))


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You were logged out')
    return redirect(url_for('show_notes'))


@app.errorhandler(500)
def server_error(e):
    return render_template('error.html', title='Server Error', error=e), 500


@app.errorhandler(404)
def not_found(e):
    return render_template('error.html', title='Page Not Found', error=''), 404


@app.errorhandler(405)
def bad_method(e):
    return redirect('/')


@app.cli.command('initdb')
def initdb_command():
    """Creates the database tables."""
    db.drop_all()
    db.create_all()
    print('Initialized the database.')
