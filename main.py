from flask import Flask, render_template, Blueprint, request
from utils2 import main_blueprint

import logging

logging.basicConfig(filename='basic.log', level=logging.INFO)

POST_PATH = 'data/data.json'
UPLOAD_FOLDER = 'static/img'

app = Flask(__name__)
app.register_blueprint(main_blueprint)

app.run(debug=True)
