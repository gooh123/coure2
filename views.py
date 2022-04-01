import utils
from flask import render_template, Blueprint, request
import logging
from exceptions import DataLayerError


views_blueprint = Blueprint('views_blueprint', __name__, template_folder='templates')
logging.basicConfig(filename='basic.log', level=logging.INFO)

DATA_FILE_PATH = 'static/data/data.json'
COMMENTS_FILE_PATH = 'static/data/comments.json'


@views_blueprint.route('/search', methods=['GET'])
def search_page():
    s = request.args.get('s', " ")
    logging.info("Выполняется поиск")
    try:
        posts = utils.search_for_posts(s)
        return render_template('search.html', posts=posts, s=s)
    except DataLayerError:
        return "поврежден файл с данными"

