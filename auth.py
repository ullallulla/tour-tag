from flask import Blueprint, render_template, redirect, url_for, request, flash
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from flask_login import login_user, logout_user, login_required

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    name = request.form.get('name')
    password = request.form.get('password')
    user = User.query.filter_by(name=name).first()
    print(user)
    #new_user = User(name=name, password=generate_password_hash(password, method='sha256'))       
    #db.session.add(new_user)
    #db.session.commit()
    if not user:
        flash('Please input login details.')
        return render_template('login.html')
    if not check_password_hash(user.password, password):
        flash('Incorrect login details.')
        return render_template('login.html')
    login_user(user)
    flash('You were successfully logged in.')
    return redirect(url_for('main.set_departure_time'))

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))