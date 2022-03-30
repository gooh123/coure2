from flask import Flask, render_template, Blueprint, request
from utils2 import main_blueprint
from utils import get_posts_all
import logging

logging.basicConfig(filename='basic.log', level=logging.INFO)

POST_PATH = 'data/data.json'
UPLOAD_FOLDER = 'static/img'


app = Flask(__name__)


@app.route('/')
def main_page():
    logging.info("запрошена главная страничка")
    return render_template('index.html')


app.run()
