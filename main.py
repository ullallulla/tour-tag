from flask import Blueprint, render_template, request, jsonify, flash, redirect, url_for
from . import db
from .ports import *


main = Blueprint('main', __name__)
departure = None

@main.route('/')
def index():
    return render_template('index.html', departure=departure, grid=unicornGrid)

@main.route('/departure', methods=["GET", "POST"])
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
    return render_template("departure.html")

@main.route('/leader', methods=["GET", "POST"])
def set_ports():
    if request.method == "POST":
        error = None

        origin_port = request.form.get('origin_port')
        destination_ports = request.form.getlist('destination_port')
        print(origin_port)
        print(destination_ports)
        if not origin_port:
            error = "Origin port is required"

        if  len(destination_ports) == 0:
            error = "Destination port is required"
        
        for port in destination_ports:
            if origin_port == port:
                error = "Origin and destination ports need to be different"
            
        if error is None:
            toggle_ports(origin_port)
            for port in destination_ports:
                toggle_ports(port)
            return render_template("leader.html")

        
        flash(error)
    return render_template("leader.html")