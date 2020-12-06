# import all necessary libraries
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect, desc
from flask import Flask, jsonify
import numpy as np
import pandas as pd
import datetime as dt

# Create a Flask app
app = Flask(__name__)

# Define static routes
@app.route("/")
def home():
    routes_available = [
        "/",
        "/api/v1.0/precipitation",
        "/api/v1.0/stations",
        "/api/v1.0/tobs",
        "/api/v1.0/<start>",
        "/api/v1.0/<start>/<end>"
    ]

    return jsonify(routes_available)


@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create engine
    engine = create_engine("sqlite:///Resources/hawaii.sqlite")

    # Reflect an existing database on a new model
    Base = automap_base()

    # Reflect the tables
    Base.prepare(engine, reflect=True)

    ## Save references to each table
    measurement = Base.classes.measurement

    ## Create session from python to the database
    session = Session(engine)

    # Calculate the latest date of the year and the date one year prior to that date
    latest_date = session.query(func.strftime(func.strftime('%Y-%m-%d', func.max(measurement.date)))).first()[0]
    latest_date = dt.datetime(int(latest_date[0:4]), int(latest_date[5:7]), int(latest_date[8:10]))
    date_a_year_ago = latest_date - dt.timedelta(days=365)

    # Query the precipitation data from the past one year
    prcp_scores = session.query(measurement.date, measurement.prcp)\
        .filter(measurement.date <= latest_date)\
        .filter(measurement.date >= date_a_year_ago)\
        .all()

    # populate the result dictiontionary
    prcp_dict = {}
    for record in prcp_scores:
        prcp_dict[str(record[0])] = record[1]

    # jsonify the output
    return jsonify(prcp_dict)

@app.route("/api/v1.0/stations")
def stations():
    # Create engine
    engine = create_engine("sqlite:///Resources/hawaii.sqlite")

    # Reflect an existing database on a new model
    Base = automap_base()

    # Reflect the tables
    Base.prepare(engine, reflect=True)

    ## Save references to each table
    station = Base.classes.station

    ## Create session from python to the database
    session = Session(engine)

    # Query all the stations
    stations = session.query(station.station).group_by(station.station).all()

    # Populate the result list
    result = []
    for i in stations:
        result.append(i[0])

    # Jsonify the result 
    return jsonify(result)

@app.route("/api/v1.0/tobs")
def tobs():

    # Create engine
    engine = create_engine("sqlite:///Resources/hawaii.sqlite")

    # Reflect an existing database on a new model
    Base = automap_base()

    # Reflect the tables
    Base.prepare(engine, reflect=True)

    ## Save references to each table
    measurement = Base.classes.measurement

    ## Create session from python to the database
    session = Session(engine)

    # Calculate the latest date of the year and the date one year prior to that date
    latest_date = session.query(func.strftime(func.strftime('%Y-%m-%d', func.max(measurement.date)))).first()[0]
    latest_date = dt.datetime(int(latest_date[0:4]), int(latest_date[5:7]), int(latest_date[8:10]))
    date_a_year_ago = latest_date - dt.timedelta(days=365)

    # Query the most active station
    most_active_station = session.query(measurement.station, func.count(measurement.station))\
        .group_by(measurement.station)\
        .order_by(desc(func.count(measurement.station)))\
        .first()[0]

    # Query the data from the most active station
    tobs = session.query(measurement.date, measurement.tobs)\
        .filter(measurement.date <= latest_date)\
        .filter(measurement.date >= date_a_year_ago)\
        .filter(measurement.station == most_active_station)\
        .all()

    # Populate the result
    result = {}
    for t in tobs:
        result[t[0]] = t[1]

    # Jsonify the result
    return jsonify(
        {
            "Data from the most Active Station": result,
            "Most Active Station": most_active_station
        }
    )

@app.route("/api/v1.0/<start>")
def tempurature_start(start):
    # Create engine
    engine = create_engine("sqlite:///Resources/hawaii.sqlite")

    # Reflect an existing database on a new model
    Base = automap_base()

    # Reflect the tables
    Base.prepare(engine, reflect=True)

    ## Save references to each table
    measurement = Base.classes.measurement

    ## Create session from python to the database
    session = Session(engine)

    ## Calulate the stats info based on the start date
    Tmin = session.query(func.min(measurement.tobs)).filter(measurement.date >= start).first()[0]
    Tmax = session.query(func.max(measurement.tobs)).filter(measurement.date >= start).first()[0]
    Tavg = session.query(func.avg(measurement.tobs)).filter(measurement.date >= start).first()[0]

    # Jsonify the result
    return jsonify(
        {
            "Minimum Tempurature": Tmin,
            "Maximum Tempurature": Tmax,
            "Average Tempurature": Tavg
        }
    )

@app.route("/api/v1.0/<start>/<end>")
def tempurature_start_end(start, end):
    # Create engine
    engine = create_engine("sqlite:///Resources/hawaii.sqlite")

    # Reflect an existing database on a new model
    Base = automap_base()

    # Reflect the tables
    Base.prepare(engine, reflect=True)

    ## Save references to each table
    measurement = Base.classes.measurement

    ## Create session from python to the database
    session = Session(engine)

    ## Calulate the stats info based on the start and end date
    Tmin = session.query(func.min(measurement.tobs))\
        .filter(measurement.date >= start).filter(measurement.date <= end).first()[0]
    Tmax = session.query(func.max(measurement.tobs))\
        .filter(measurement.date >= start).filter(measurement.date <= end).first()[0]
    Tavg = session.query(func.avg(measurement.tobs))\
        .filter(measurement.date >= start).filter(measurement.date <= end).first()[0]

    # Jsonify the result
    return jsonify(
        {
            "Minimum Tempurature": Tmin,
            "Maximum Tempurature": Tmax,
            "Average Tempurature": Tavg
        }
    )

# Define main behavior
if __name__ == "__main__":
    app.run(debug=True)
