# Import the dependencies.
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
measurement= Base.classes.measurement
station= Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)
#session.close()
#################################################
# Flask Setup
#################################################


app = Flask(__name__)

#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/startYYYYMMDD<br/>"
        f"/api/v1.0/startYYYYMMDD/endYYYYMMDD"
    )
  
@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)

    prec_scores=session.query(measurement.date, measurement.prcp).filter(measurement.date >= '2016-08-23').order_by(measurement.date).all()
    session.close()

    year_prec = []
    for date, prcp in prec_scores:
        prec_dict = {}
        prec_dict[date] = prcp
        year_prec.append(prec_dict)

    return jsonify(year_prec)

@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    locations = session.query(measurement.station).group_by(measurement.station).all()
    locations_list=list(np.ravel(locations))
    session.close()
    return jsonify(locations_list)
    

@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)
    year_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    location_year=session.query(measurement.tobs).filter(measurement.station=="USC00519281").filter(measurement.date>=year_date).all()
    year_list=list(np.ravel(location_year))
    session.close()
    return jsonify(year_list)
    

@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")
def date(start=None, end=None):
    session = Session(engine)
    start=dt.datetime.strptime(start, "%Y%m%d")
    if not end:
        location_active=session.query(func.min(measurement.tobs), func.max(measurement.tobs), func.avg(measurement.tobs)).filter(measurement.station=="USC00519281").filter(measurement.date>=start).all()
        location_start=list(np.ravel(location_active))

        session.close()
        return jsonify(location_start)
    end=dt.datetime.strptime(end, "%Y%m%d")
    location_active_end=session.query(func.min(measurement.tobs), func.max(measurement.tobs), func.avg(measurement.tobs)).filter(measurement.station=="USC00519281").filter(measurement.date>=start).filter(measurement.date<=end).all()
    location_end=list(np.ravel(location_active_end))
    session.close()
    return jsonify(location_end)



if __name__ == '__main__':
    app.run(debug=True)


