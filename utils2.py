from flask import render_template, Blueprint, request
import logging
from utils import get_posts_all, load_json_from_file
from exceptions import DataLayerError

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')
logging.basicConfig(filename='basic.log', level=logging.INFO)
DATA_FILE_PATH = 'static/data/data.json'


@main_blueprint.route('GET/')
def main_page():
    logging.info("запрошена главная страничка")
    return render_template("index.html")


@main_blueprint.route('/search')
def search_page():
    s = request.args.get('s', "")
    function = load_json_from_file(DATA_FILE_PATH)
    logging.info("Выполняется поиск")
    try:
        posts = function.get_posts_all(s)
        return render_template("search.html", posts=posts, s=s)
    except DataLayerError:
        return "поврежден файл с данными"
