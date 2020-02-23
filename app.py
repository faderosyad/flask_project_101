#Fade Khalifah Rosyad
#faderosyad@gmail.com
#Started: 13 January 2020

#Main script for Flask Web Application

import requests, json
from flask import Flask, render_template, request, json
from datetime import datetime, timedelta

app = Flask(__name__)

def getTimestamp():
    return datetime.now().strftime("%d-%m-%Y %H:%M:%S") + timedelta(hour=7)

@app.route('/')
def hello_world():
    dateTime = getTimestamp()
    helloMessage = "Hello World! \n Today date is "
    return render_template('fronpage.html', helloMessage = helloMessage, dateTime = dateTime)

@app.route('/iseng')
def testing():
    name = "Fade Khalifah Rosyad"
    return name

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True, port= 2323)
