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
    if request.method == 'POST':
        if password == 'Driver':
            #Mainly to help in testing, name functionality can be removed if necessary
            if name != "":
                new_user = User(name=name, password=generate_password_hash(password, method='sha256'))       
                db.session.add(new_user)
                db.session.commit()
                user = User.query.filter_by(name=name).first()
                login_user(user)
                flash('You were successfully logged in as a driver.')
                return redirect(url_for('main.set_departure_time'))
            else:
                flash('Name is required')
        else:
            flash('Please check your login details and try again.')
    return render_template('login.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))