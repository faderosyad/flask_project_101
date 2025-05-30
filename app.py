# Fade Khalifah Rosyad
# faderosyad@gmail.com
# Started: 13 January 2020
# Vibe coding with Gemini

# Main script for Flask Web Application
from flask import Flask
from routes.main_routes import main_bp # Import the Blueprint

app = Flask(__name__)

# Configuration can remain here
app.config['MONGIDB_SETTINGS'] = {
    'host': 'mongodb://localhost/movie-bag'
    }

# Register the Blueprint
app.register_blueprint(main_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True, port= 2323)
