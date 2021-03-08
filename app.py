from flask import Flask, render_template, request, jsonify, flash, redirect
import time




app = Flask(__name__)
app.secret_key = "hello"


@app.route('/')
def index():
    return render_template('index.html')


#def selectPorts():
    unicornGrid = [[0]*8 for i in range(8)]

    listOfCities = [Aland, Turku, Helsinki, Hamina, Pori, Vaasa, Kokkola, Oulu]

# POST request for departure time


@app.route('/departure', methods=["GET", "POST"])
def foo():
    if request.method == "POST":
        error = None
        departureTime = request.form["departureTime"]

        if not departureTime:
            error = "Time is required"

        if error is None:
            print('departure time', departureTime)
            return redirect('/')

        flash(error)
    return render_template("departure.html")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


# komentorivillä python app.py
#
# netti sivu löytyy:
# http://127.0.0.1:5000/
