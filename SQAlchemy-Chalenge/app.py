#import dependencies
import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify



#database setup
engine = create_engine("sqlite:///hawaii.sqlite")

#reflect 
Base = automap_base()
Base.prepare(engine, reflect=True)

#save table references
Measurement = Base.classes.measurement
Station = Base.classes.station

#create session link 
session = Session(engine)


#flask setup
app = Flask(__name__)



#create routes

@app.route("/")
def welcome():
    return (
        f"Welcome to the Climate Analysis API!<br/>"
        f"Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/temp/start/end"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return the precipitation data"""

    #query for the date and precipitation
    precipitation = session.query(Measurement.date, Measurement.prcp).all()

    #convert to list and return results 
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)


@app.route("/api/v1.0/stations")
def stations():
    """Return a list of stations."""
    #query for station list
    results = session.query(Station.station).all()
    #convert to list and return results 
    stations = list(np.ravel(results))
    return jsonify(stations)


@app.route("/api/v1.0/tobs")
def temp_obs():
    """Return the temperature observations for previous year."""
    #calculate temp 1 yr from date
    prev_yr = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    # Query the primary station for all tobs from the last year
    results = session.query(Measurement.tobs).filter(Measurement.date >= prev_year).all()

    #convert to list and return results
    temps = list(np.ravel(results))
    return jsonify(temps)


@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def stats(start=None, end=None):
    """Return TMIN, TAVG, TMAX."""

    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        #calculate TMIN, TAVG, TMAX when only given start date
        results = session.query(*sel).filter(Measurement.date >= start).all()
        #convert to list and return results
        temps = list(np.ravel(results))
        return jsonify(temps)

    #calculate TMIN, TAVG, TMAX when given start and end date
    results = session.query(*sel).filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    #convert to list and return results 
    temps = list(np.ravel(results))
    return jsonify(temps)


if __name__ == '__main__':
    app.run()