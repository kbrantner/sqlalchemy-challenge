# sqlalchemy-challenge

#Description
For this project I decided to do a climate analysis for Honolulu, HI using both Python and SQLAlchemy. The data for this analysis is in a SQLite database that has the classes “station” and “measurement”. First, I looked at the past 12 months of precipitation data, which was saved to a DataFrame The results are then presents using the plot method. It is important to note that the graph only shows the days that had precipitation. I also looked that the summary statistics for this data using Pandas. 

For the second part of this project, I took a detailed look at the 9 stations in the dataset. I found the most active station, which is “USC00519281”. I calculated the lowest, highest, and average temperature from that station. I then created a histogram of the last 12 months of temperature observations from this station. The histogram data is divided into 12 bins. 

For the final part of this project, I designed a Flask API based on my code from the previous parts of this project. The Flask has both static and dynamic routes, all of which are displayed on the homepage. For the dynamic routes you only enter the start’s “YYYMMDD” or the start and end date separated by a “/”, for example “YYYMMDD/ YYYMMDD”.

#Visuals
Precipitation Graph
 
Histogram of Temperatures from Most Active Station
 
#Installation
To work with sqlalchemy in jupyter notebook and to create the graphs, import the following:
%matplotlib inline
from matplotlib import style
style.use('fivethirtyeight')
import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

To create Flask API in a python file, import the following:
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt
from flask import Flask, jsonify

#Support
If help is needed with SQLalchemy or Flask API, I recommend searching Stack Overflow for the answers to specific questions.  

#Authors and acknowledgment
This project was completed by Kelsey Brantner. Bethany Lindberg helped me understand how to have my precipitation graph displayed correctly. Additionally, she helped me understand how to setup my app.py routes to accept dynamic start and end date parameters.  Then the following link helped me understand how to rotate my x_ticks, so the dates were more readable https://stackoverflow.com/questions/24524104/pandas-describe-is-not-returning-summary-of-all-columns. The following link helped me understand how to set the axis labels on a histogram https://stackoverflow.com/questions/59482310/how-to-show-variable-names-as-labels-on-the-x-axis-of-a-histogram. Additionally, I received help from Bethany Lindberg helped me understand how to setup my app.py routes that accept start and end date parameters. 

#Resources
According to the files’ source site, “Menne, M.J., I. Durre, R.S. Vose, B.E. Gleason, and T.G. Houston, 2012: An overview of the Global Historical Climatology Network-Daily Database. Journal of Atmospheric and Oceanic Technology, 29, 897-910, https://journals.ametsoc.org/view/journals/atot/29/7/jtech-d-11-00103_1.xml”

#Project status
At this time, the project is considered complete. 
