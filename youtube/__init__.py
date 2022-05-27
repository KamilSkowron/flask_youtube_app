from flask import Flask, render_template, request, Response, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from flask_restx import Api, Resource


# Start application
app = Flask(__name__)

# Configuration of the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 'Secret key' --> hide it later
app.config['SECRET_KEY'] = 'ec9439cfc6c796ae2029594d'

# Upload file for video pics
UPLOAD_FOLDER = 'youtube/static/images/video_pics'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Connect app with database
db = SQLAlchemy(app)

api = Api(app)

from youtube import routes
from youtube import restAPI