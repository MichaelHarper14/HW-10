# 1. import Flask
from flask import Flask
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


Base = automap_base()
Base.prepare(engine, reflect=True)
date = Base.classes.precipitation






# 2. Create an app
app = Flask(__name__)


@app.route("/")
def home():
    print("Homee")
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        )



@app.route("/api/v1.0/precipitation")
def Precipitation():
    print("Rain Fall") 
    session1 = session.query(Measurement.date, Measurement.prcp)\
                filter(Measurement.date >= year_range.date).\
                    group_by(Measurement.date).all()

    session.close()
    all_precipitation = list(np.ravel(results))

 
    Precipitation_Dictionary = []
    for date, prcp in results:
        date_dict = {}
        date_dict["precipitation"] = prcp
        Precipitation_Dictionary.append(date_dict)

    return jsonify(Precipitation_Dictionary)
    

@app.route("/api/v1.0/stations")
def Station():
    print("Weather Stations")
  station_results = session.query(Station.station).all()
    return jsonify(station_results)




@app.route("/api/v1.0/tobs")
def TOBS():
    print("Observations")
TOBS_Results = session.query(Measurement.date,Measurement.tobs)./
                filter(Measurement.date)>= year_range.date).\
                    group_by(Measurement.date).all()
    return jsonify(TOBS_Results)




@app.route("/api/v1.0/<start>")
def daily_normals(start): 
    Print("Start")
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
    results = session.query(*sel).filter( Measurement.date >= start).all()
    daily_normals = list(np.ravel(results))
    return jsonify(daily_normals)


@app.route("/api/v1.0/<start>/<end>")
def trip_temp(start=None,end=None):
    Print("End")
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
    results = session.query(*sel).filter(Measurement.date >= start, Measurement.date <= end).all()
    trip_temp = list(np.ravel(results))
    return jsonify(trip_temp)


if __name__ == "__main__":
    app.run(debug=True)
© 2019 GitHub, Inc.