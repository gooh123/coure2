from flask import Blueprint, render_template, request
import logging
from utils import load_json_from_file

DATA_FILE_PATH = 'static/data/data.json'

views_blueprint = Blueprint('views_blueprint', __name__, template_folder='template')
logging.basicConfig(filename="basic.log", level=logging.INFO)


@views_blueprint.route('/comments')
def post_info():
    data = load_json_from_file(DATA_FILE_PATH)
    information = []
    for info in data:
        if info in data["content"]:
            information.append(data)

        return information
    return render_template('post.html')


