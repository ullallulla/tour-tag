from flask import Blueprint, render_template, request, jsonify, flash, redirect, url_for
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login', methods = ['GET', 'POST'])
def login():
    login_error = None
    if request.method == 'POST':
        if request.form['password'] == 'Driver':
            flash('You were successfully logged in as a driver.')
            return redirect(url_for('main.set_departure_time'))
        else:
            login_error = 'Invalid password.'
    return render_template('login.html')

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/logout')
def logout():
    return 'Logout'