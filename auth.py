from flask import Blueprint, render_template, redirect, url_for, request, flash, session
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

    boat_name = request.form.get('boat_name')
    
    session['boat_name'] = boat_name

    #print(user)
    if not user:
        flash('Please input login details.')
        return render_template('login.html')
    if not check_password_hash(user.password, password):
        flash('Incorrect login details.')
        return render_template('login.html')
    if not boat_name:
        flash('Please input login details.')
        return render_template('login.html')
    login_user(user)
    #print(boat_name)

    if name == 'Driver':
        return redirect(url_for('main.set_departure_time'))
    if name == 'Leader':
        return redirect(url_for('main.set_ports'))

# /signup page for account generation purposes
""" @auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')
        new_user = User(name=name, password=generate_password_hash(password, method='sha256'))       
        db.session.add(new_user)
        db.session.commit()
        flash('Database succesfully updated.')
        return render_template('signup.html')
    return render_template('signup.html')
 """
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))

