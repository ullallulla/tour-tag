from flask import Flask, render_template, request, g
import time



app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')





if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')



# komentorivillä python app.py
# 
# netti sivu löytyy: 
# http://127.0.0.1:5000/