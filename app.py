from flask import Flask, render_template, request, jsonify, flash, redirect, url_for
import time

from flask.helpers import url_for




app = Flask(__name__)
app.secret_key = "hello"


departure = None

@app.route('/')
def index():
    return render_template('index.html', departure=departure)


#def selectPorts():
    unicornGrid = [[0]*8 for i in range(8)]

    listOfCities = [Aland, Turku, Helsinki, Hamina, Pori, Vaasa, Kokkola, Oulu]

# POST request for departure time


@app.route('/departure', methods=["GET", "POST"])
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
            return redirect(url_for('index'))


        flash(error)
    return render_template("departure.html")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


# komentorivillä python app.py
#
# netti sivu löytyy:
# http://127.0.0.1:5000/
