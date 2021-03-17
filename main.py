from flask import Blueprint, render_template, request, jsonify, flash, redirect, url_for
from flask_login import login_required, current_user
from . import db
from .models import User
from .ports import *
import datetime

main = Blueprint('main', __name__)

departure = None
origin_port = None
destination_ports = None
next_port = None
current_port = None
success = None
@main.route('/')
def index():
    return render_template('index.html', success=success, departure=departure, origin_port=origin_port, destination_ports=destination_ports, next_port=next_port, current_port=current_port, grid=unicornGrid)

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
@login_required
def set_ports():
    if request.method == "POST":
        error = None
        global origin_port
        global current_port
        global next_port
        global destination_ports
        global success
        success = None
        origin_port = request.form.get('origin_port')
        current_port = request.form.get('current_port')
        next_port = request.form.get('next_port')
        destination_ports = request.form.getlist('destination_port')
        print(origin_port)
        print(destination_ports)
        print(request.form.get('reset'), 'reset')
        if request.form.get('reset') == 'Reset ports':
            print('asd')
            clear_ports()
            return redirect(url_for('main.set_ports'))
        if not origin_port:
            error = "Origin port is required"

        if  len(destination_ports) == 0:
            error = "Destination port is required"

        if not current_port:
            error = "Current port is required"

        if next_port not in destination_ports:
            error = "Next port needs to be a destination port"
            
        for port in destination_ports:
            if origin_port == port:
                error = "Origin and destination ports need to be different"

        if error is None:
            clear_ports()
            success = True
            toggle_ports(origin_port)
            for port in destination_ports:
                toggle_ports(port)
            return render_template("stateupdate.html", grid=unicornGrid, name=current_user.name, destination_ports=destination_ports)


        
        flash(error)
    return render_template("leader.html", grid=unicornGrid, name=current_user.name)

@main.route('/update', methods=["GET", "POST"])
@login_required
def state_update():
    print(destination_ports)
    if not origin_port:
        return redirect(url_for('main.set_ports'))
    if len(destination_ports) == 0:
        return redirect(url_for('main.set_ports'))
    if request.method == "POST":
        error = None
        success = None
        global current_port
        global next_port
        global new_next_port
        arrival_port = next_port
        new_next_port = request.form.get('next_port')

        if new_next_port not in destination_ports:
            error = "Next port needs to be a destination port"
        
        if new_next_port == next_port and len(destination_ports) != 1:
            error = "New destination needs to be a different port"

        if error is None:
            clear_ports()
            success = True
            toggle_ports(origin_port)
            destination_ports.remove(arrival_port)
            current_port = arrival_port
            next_port = new_next_port
            flash('Success')
            for port in destination_ports:
                toggle_ports(port)
            if len(destination_ports) == 0:
                next_port = None
                return redirect(url_for('main.set_ports'))
            return render_template("stateupdate.html", grid=unicornGrid, name=current_user.name, destination_ports=destination_ports)

        
        flash(error)
    return render_template("stateupdate.html", grid=unicornGrid, name=current_user.name, destination_ports=destination_ports)
