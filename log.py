import datetime
from sqlalchemy.ext.declarative.api import as_declarative
from .models import Data
from . import db
from flask import session

class Logkeeper():

    def lgwrite(self,message):
        try:
            ct = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            message = ct + " " + message + "\n"
            logfile = open("log.txt","a+")
            logfile.write(message)
            logfile.close()
        except:
            print("Failed to write log")

def log_arrival(next_port):
    boat = session.get('boat_name', None)
    port = next_port
    arrival_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    arrival_data = Data(boat_id=boat, port=port, arrival_time=arrival_time)       
    db.session.add(arrival_data)
    db.session.commit()

def log_departure(next_port):
    boat = session.get('boat_name', None)
    port = next_port
    departure_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    departure_data = Data(boat_id=boat, port=port, departure_time=departure_time)       
    db.session.add(departure_data)
    db.session.commit()
