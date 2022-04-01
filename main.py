from flask import Flask, render_template, Blueprint, request
from utils2 import main_blueprint
from views import views_blueprint
from api.routes import api_bp
import logging

logging.basicConfig(filename='basic.log', level=logging.INFO)

POST_PATH = 'data/data.json'
UPLOAD_FOLDER = 'static/img'

app = Flask(__name__)
app.register_blueprint(main_blueprint)
app.register_blueprint(views_blueprint)
app.register_blueprint(api_bp)

app.run(debug=True)
