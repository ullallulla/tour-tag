from flask import Blueprint, render_template, request, jsonify, flash, redirect, url_for
from flask_login import login_required, current_user
from . import db
from .models import User


main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')

@main.route('/departure', methods=["GET", "POST"])
@login_required
def set_departure_time():
    if request.method == "POST":
        error = None
        departure_time = request.form["departure_time"]

        if not departure_time:
            error = "Time is required"

        if error is None:
            global departure
            departure = departure_time
            print('departure time', departure_time)
            return redirect(url_for('main.index'))

        flash(error)
    return render_template("departure.html", name=current_user.name)