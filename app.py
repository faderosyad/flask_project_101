# Fade Khalifah Rosyad
# faderosyad@gmail.com
# Started: 13 January 2020

# Main script for Flask Web Application

import requests, json
from flask import Flask, render_template, request, json, Response, jsonify
from datetime import datetime, timedelta

from resource.movie import movies

from database.db import initialize_db
from database.models import Movie

app = Flask(__name__)

app.config['MONGIDB_SETTINGS'] = {
    'host': 'mongodb://localhost/movie-bag'
    }

initialize_db(app)
app.register_blueprint(movies)

def getTimestamp():
    nowDateTime = datetime.now() + timedelta(hours=7)
    formatDateTime = nowDateTime.strftime("%d-%m-%Y %H:%M:%S")
    return formatDateTime

@app.route('/')
def frontpage():
    dateTime = getTimestamp()
    helloMessage = "Hello World! \n Today date is "
    return render_template('frontpage.html', helloMessage = helloMessage, dateTime = dateTime)

@app.route('/about_me')
def about_me():
    name = "Fade Khalifah Rosyad"
    jobs = "Software Development Engineer"
    linkedin = "https://www.linkedin.com/in/faderosyad/"
    github = "https://github.com/faderosyad"
    return render_template('aboutme.html', name = name, jobs = jobs, linkedin = linkedin, github = github)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True, port= 2323)
