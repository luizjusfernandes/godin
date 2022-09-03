from flask import abort, Flask, jsonify, request, render_template
import sqlite3

# Create application instance
app = Flask(__name__)

@app.route('/')
def index():
    """Query database for turtles"""

    return 'padre'