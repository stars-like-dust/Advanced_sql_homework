from flask import Flask, jsonify

import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt

app = Flask(__name__)

engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

Base.classes.keys()

Measurement = Base.classes.measurement
Station = Base.classes.station

session = Session(engine)


# Calculate the date 1 year ago from today
#print(dt.date.today())
#year_ago = dt.date.today() - dt.timedelta(days=365)
#year_ago

# Perform a query to retrieve the data and precipitation scores

#year = session.query(Measurement.date,Measurement.prcp).filter(
#Measurement.date > year_ago).order_by(Measurement.date).all()


#Query 1 prcp

prcp=session.query(Measurement.date, Measurement.prcp).filter(Measurement.date > '2016-09-23' ).order_by(Measurement.date).all()

prcp_date = set([i[0] for i in prcp])

prcp_all={}
for i in prcp_date:
   vals=[]
   for j in range(len(prcp)):
       if prcp[j][0] == i:
           temp=prcp[j][1]
           vals.append(temp)
   prcp_all[i]=vals

#Query 2 stations

stats = session.query(Measurement.station, Measurement.id).all()

#Query 3 tobs
tobs=session.query(Measurement.date, Measurement.tobs).filter(Measurement.date > '2016-09-23' ).order_by(Measurement.date).all()

tobs_date = set([i[0] for i in tobs])

tobs_all={}
for i in tobs_date:
   vals=[]
   for j in range(len(prcp)):
       if prcp[j][0] == i:
           temp=tobs[j][1]
           vals.append(temp)
   tobs_all[i]=vals

#Query 4
#Query for the dates and temperature observations from the last year.
#Convert the query results to a Dictionary using `date` as the key and `tobs` as the value.
#Return the JSON representation of your dictionary.

#HOME_________________________________________________________________________________________________________________________

@app.route('/')

def Hello():
    return(
        'Congrats you found the Hawaii API the coolest API around rated by meeeeeeeeeee'
    )


#Routes__________________________________________________________________________________________________________________________-

#Route 1

@app.route("/api/v1.0/precipitation")
def precipitation():
   """Return the test data as json"""
   return jsonify(prcp_all)

#Route 2

#Route 3

@app.route("/api/v1.0/tobs")
def tobs_1():
   """Return the test data as json"""
   return jsonify(tobs_all)

#route 4












