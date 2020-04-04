# Fade Khalifah Rosyad
# faderosyad@gmail.com
# Started: 13 January 2020

# Main script for Flask Web Application

import requests, json
from flask import Flask, render_template, request, json, Response
from datetime import datetime, timedelta

from database.db import initialize_db
from database.models import Movie

app = Flask(__name__)

app.config['MONGIDB_SETTINGS'] = {
    'host': 'mongodb://localhost/movie-bag'
    }

initialize_db(app)

@app.route('/movies')
def get_movies():
    movies = Movie.objects().to_json()
    return Response(movies, mimetype="application/json", status=200)

@app.route('/movies', methods=['POST'])
def add_movies():
    body = request.get_json()
    movie = Movie(**body).save()
    id = movie.id
    return {'id': str(id)}, 200

@app.route('/movies/<id>', methods=['PUT'])
def update_movie(id):
    body = request.get_json()
    Movie.objects.get(id = id).update(**body)
    return '',200

@app.route('/movies/<id>', methods=['DELETE'])
def delete_movie(id):
    Movie.objects.get(id = id).delete()
    return '', 200

@app.route('/movies/<id>')
def get_movie(id):
    movies = Movies.objects.get(id = id).to_json()
    return Response(movies, mimetype="application/json", status=200)


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
