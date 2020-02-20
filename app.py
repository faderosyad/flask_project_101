#Fade Khalifah Rosyad
#faderosyad@gmail.com
#Started: 13 January 2020

#Main script for Flask Web Application

import requests, json
from flask import Flask, render_template, request, json
from datetime import datetime

def getTimestamp():
    return datetime.now().strftime("%d-%m-%Y %H:%M:%S")

app = Flask(__name__)

@app.route('/')
def hello_world():
    date = getTimestamp()
    textToOut = "Hello World! \n Today date is " + date 
    return textToOut

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True, port= 2323)
