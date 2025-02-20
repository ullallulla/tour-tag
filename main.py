from flask import Blueprint, render_template, request, jsonify, flash, redirect, url_for, session
from flask_login import login_required, current_user
from . import db
from .models import Data
from .ports import *
from .colors import *
from .log import *

main = Blueprint('main', __name__)

origin_port = None
destination_ports = None
next_port = None
current_port = None


@main.route('/')
def index():
    departure = session.get('departure_time', None)
    return render_template('index.html', departure=departure, origin_port=origin_port, destination_ports=destination_ports, next_port=next_port, current_port=current_port)

@main.route('/departure', methods=["GET", "POST"])
@login_required
def set_departure_time():
    boat_name = session.get('boat_name', None)

    if request.method == "POST":
        error = None
        departure_time = request.form["departure_time"]
        if not departure_time:
            error = "Time is required"

        if error is None:
            session['departure_time'] = departure_time

            
            #print('departure time', departure_time)
            return redirect(url_for('main.index'))

        flash(error)
    return render_template("departure.html", name=current_user.name, boat_name=boat_name)

@main.route('/leader', methods=["GET", "POST"])
@login_required
def set_ports():

    boat_name = session.get('boat_name')

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
            #print('origin port',origin_port_new)
            #print('destination port',destination_ports_new)
            #print(request.form.get('reset'), 'reset')
            
            current_port = origin_port

            for port in destination_ports_new:
                if port == "":
                    error = "Destination port can't be empty"


            if not origin_port_new:
                error = "Origin port is required"

            elif len(destination_ports_new) == 1 and destination_ports_new[0] == '':
                error = "Destination port is required"


            else:
                origin_port = origin_port_new
                destination_ports = destination_ports_new
                #print(destination_ports)
                set_origin_port_color(origin_port)
                set_destination_port_color(destination_ports)



        if request.form.get('update') == 'Update':
            if request.form.get('next_port') == '':
                error = 'Next port is required'
            else:
                next_port = request.form.get('next_port')
                #print(request.form.get('next_port'))
                set_next_port_color(next_port)
                return redirect(url_for('main.set_ports'))


        if request.form.get('reset') == 'Reset ports':
            clear_ports()
            origin_port = None
            destination_ports = None
            next_port = None

            return redirect(url_for('main.set_ports'))



        if request.form.get('arrived-button') == 'Arrived':
            departed = session.get('departed')

            if next_port == None:
                error = ('No destination set, please set the destination via ''Next port''')
            elif departed is not True:
                error = "You haven't departed yet"
            else:
                set_arrived(next_port, destination_ports)
                log_arrival(next_port)
                session['departed'] = False
                current_port = next_port
                next_port = None
                
                return redirect(url_for('main.set_ports'))



        if request.form.get('departed-button') == 'Departed':
            departed = session.get('departed')
            #print(departed)
            if next_port is None:
                error = 'Next port needs to be set before departure'
            elif departed is True:
                error = "You have already departed"
            else:
                #print('departed')
                set_departed(next_port, current_port, origin_port)
                log_departure(next_port)
                session['departed'] = True
                session['departure_time'] = None
                return redirect(url_for('main.set_ports'))




        if error is None:
            
            return redirect(url_for('main.set_ports'))
        
        flash(error)

    return render_template("leader.html", name=current_user.name, destination_ports=destination_ports, boat_name=boat_name, origin_port=origin_port, next_port=next_port)



@main.route('/data/<boat>')
@login_required
def boat_search(boat):
    
    
    boat_data = Data.query.filter_by(boat_id=boat).all()

    boat_list = []
        


    for boat in boat_data:
         boat_dict = {}
         boat_dict['id']=boat.id
         boat_dict['boat']=boat.boat_id
         boat_dict['port']=boat.port
         boat_dict['arrival_time']=boat.arrival_time
         boat_dict['departure_time']=boat.departure_time
         boat_list.append(boat_dict)

    return jsonify({'boat_data' : boat_list})