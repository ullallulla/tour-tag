from flask import Blueprint, render_template, request, jsonify, flash, redirect, url_for
from flask_login import login_required, current_user
from . import db
from .models import User
from .ports import *
import datetime
from .colors import *

main = Blueprint('main', __name__)

departure = None
origin_port = None
destination_ports = None
next_port = None
current_port = None


@main.route('/')
def index():
    return render_template('index.html', departure=departure, origin_port=origin_port, destination_ports=destination_ports, next_port=next_port, current_port=current_port)

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

            origin_port = request.form.get('origin_port')
            #current_port = request.form.get('current_port')
            destination_ports = request.form.getlist('destination_port')
            next_port = request.form.get('next_port')

            print('origin port',origin_port)
            print('destination port',destination_ports)
            #print(request.form.get('reset'), 'reset')
            
            current_port = origin_port


        if request.form.get('update') == 'Update':
            next_port = request.form.get('next_port')
            return redirect(url_for('main.set_ports'))


        if request.form.get('reset') == 'Reset ports':
            print('asd')
            clear_ports()
            return redirect(url_for('main.set_ports'))



        if request.form.get('arrived-button') == 'Arrived':
            set_arrived(next_port, destination_ports)
            current_port = next_port
            next_port = None
            return redirect(url_for('main.set_ports'))



        if request.form.get('departed-button') == 'Departed':
            if next_port is None:
                error = 'Next port needs to be set before departure'
            else:
                print('departed')
                set_departed(next_port, destination_ports)
                return redirect(url_for('main.set_ports'))



        if not origin_port:
            error = "Origin port is required"

        if  len(destination_ports) == 0:
            error = "Destination port is required"

            
        for port in destination_ports:
            if origin_port == port:
                error = "Origin and destination ports need to be different"

        if error is None:
            clear_ports()
            #toggle_origin_port(origin_port)
            #for port in destination_ports:
                #toggle_destination_port(port)
            return redirect(url_for('main.set_ports'))
        
        flash(error)

    return render_template("leader.html", name=current_user.name)

