# 1. import Flask
from flask import Flask, jsonify


# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect
import datetime as dt

# 2 create an app, being sure to pass__name__
app = Flask(__name__)


engine = create_engine("sqlite:///Resources/hawaii.sqlite")
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station
# Create our session (link) from Python to the DB
session = Session(engine)

# 3 define what to do when a user hits the index route

@app.route("/")
def home():
    
    return (f"/api/v1.0/precipitation<br/>"
    f"/api/v1.0/station<br/>"
    f"/api/v1.0/tobs<br/>"
    f"/api/v1.0/start_date<br/>"
    f"/api/v1.0/start_date/end_date<br/>")

# 4 Define what to do when a user hits the /about route

@app.route("/api/v1.0/precipitation")
def prcp():
    prev_year = dt.date(2017,8,23)-dt.timedelta(365)
    results = session.query(Measurement.date, Measurement.prcp)\
    .filter(Measurement.date >= prev_year).all()

    rain_list = []
    for row in results:
        rain_list.append({"date":row[0],"prcp":row[1]})
    return jsonify(rain_list)


@app.route("/api/v1.0/station")
def station():
    total_stations = session.query(Station.name, Station.station)

    station_list = []
    for row in total_stations:
        station_list.append({"name":row[0],"station":row[1]})
    
    return jsonify(station_list)


@app.route("/api/v1.0/tobs")
def tobs():
    temps = session.query(Measurement.tobs, Measurement.date).filter\
                            (Measurement.station == "USC00519281")

    temp_list = [] 
    for row in temps:
        temps.append({"tobs":row[0],"date":row[1]})

    return jsonify(temp_list)  


if __name__ == "__main__":
    app.run(debug=True)




