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

        if request.form.get('submit') == 'Submit':

            origin_port_new = request.form.get('origin_port')
            #current_port = request.form.get('current_port')
            destination_ports_new = request.form.getlist('destination_port')

            print('origin port',origin_port_new)
            print('destination port',destination_ports_new)
            #print(request.form.get('reset'), 'reset')
            
            current_port = origin_port


            if not origin_port_new:
                error = "Origin port is required"

            elif len(destination_ports_new) == 1 and destination_ports_new[0] == '':
                error = "Destination port is required"

            else:
                origin_port = origin_port_new
                destination_ports = destination_ports_new
                #set_origin_port_color(origin_port)
                #set_destination_port_color(destination_ports)



        if request.form.get('update') == 'Update':
            if request.form.get('next_port') == '':
                error = 'Next port is required'
            else:
                next_port = request.form.get('next_port')
                print(request.form.get('next_port'))
                #set_next_port_color(next_port)
                return redirect(url_for('main.set_ports'))


        if request.form.get('reset') == 'Reset ports':
            print('asd')
            clear_ports()
            origin_port = None
            destination_ports = None
            next_port = None

            return redirect(url_for('main.set_ports', destination_ports=destination_ports))



        if request.form.get('arrived-button') == 'Arrived':
            if next_port == None:
                error = ('No destination set, please set the destination via ''Next port''')
            else:
                set_arrived(next_port, destination_ports)
                current_port = next_port
                next_port = None
                return redirect(url_for('main.set_ports', destination_ports=destination_ports))



        if request.form.get('departed-button') == 'Departed':
            if next_port is None:
                error = 'Next port needs to be set before departure'
            else:
                print('departed')
                set_departed(next_port, current_port, origin_port)
                return redirect(url_for('main.set_ports', destination_ports=destination_ports))


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
            toggle_origin_port(origin_port)
            for port in destination_ports:
                toggle_destination_port(port)
            return redirect(url_for('main.state_update'))
        
        flash(error)
    return render_template("leader.html", grid=unicornGrid, name=current_user.name)

@main.route('/update', methods=["GET", "POST"])
@login_required
def state_update():
    if not origin_port:
        return redirect(url_for('main.set_ports'))
    if len(destination_ports) == 0:
        return redirect(url_for('main.set_ports'))
    global new_destination_ports
    new_destination_ports = destination_ports.copy()
    global next_port
    arrival_port = next_port
    if len(new_destination_ports) == len(destination_ports):
        new_destination_ports.remove(arrival_port)
    if request.method == "POST":
        error = None
        success = None
        global current_port
        global new_next_port
        new_next_port = request.form.get('next_port')
        if new_next_port != 'Arrival':
            if new_next_port not in destination_ports:
                error = "Next port needs to be a destination port"

        if error is None:
            clear_ports()
            success = True
            toggle_origin_port(origin_port)
            toggle_origin_port(arrival_port)
            current_port = arrival_port
            destination_ports.remove(arrival_port)
            next_port = new_next_port
            flash('Success')
            for port in destination_ports:
                toggle_destination_port(port)
            if len(destination_ports) == 0:
                next_port = None
                return redirect(url_for('main.set_ports'))
            return redirect(url_for('main.state_update'))

        
        flash(error)
    return render_template("stateupdate.html", grid=unicornGrid, name=current_user.name, new_destination_ports=new_destination_ports)
