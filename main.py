from flask import Blueprint, render_template, request, jsonify, flash, redirect, url_for
from flask_login import login_required, current_user
from . import db
from .models import User
from .ports import *
import datetime

main = Blueprint('main', __name__)

departure = None

@main.route('/')
def index():
    return render_template('index.html', departure=departure, grid=unicornGrid)

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

@main.route('/leader', methods=["GET", "POST"])
def set_ports():
    if request.method == "POST":
        error = None

        origin_port = request.form.get('origin_port')
        destination_ports = request.form.getlist('destination_port')
        print(origin_port)
        print(destination_ports)
        print(request.form.get('reset'), 'reset')
        if request.form.get('reset') == 'Reset ports':
            print('asd')
            clear_ports()
            return render_template("leader.html",grid=unicornGrid)
        if not origin_port:
            error = "Origin port is required"

        if  len(destination_ports) == 0:
            error = "Destination port is required"
        
        for port in destination_ports:
            if origin_port == port:
                error = "Origin and destination ports need to be different"
            
        if error is None:
            clear_ports()
            toggle_ports(origin_port)
            for port in destination_ports:
                toggle_ports(port)
            return render_template("leader.html",grid=unicornGrid)

        
        flash(error)
    return render_template("leader.html", grid=unicornGrid)
