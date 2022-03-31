from flask import render_template, Blueprint, request
import logging
from utils import get_posts_all, load_json_from_file, search_for_posts
from exceptions import DataLayerError

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')
logging.basicConfig(filename='basic.log', level=logging.INFO)
DATA_FILE_PATH = 'static/data/data.json'


@main_blueprint.route('/')
def main_page():
    data = load_json_from_file(DATA_FILE_PATH)
    logging.info("запрошена главная страничка")
    return render_template('index.html', information="content", posts=data)


@main_blueprint.route('/search')
def search_page():
    s = request.args.get('s', "")
    logging.info("Выполняется поиск")
    try:
        posts = search_for_posts(s)
        return render_template('search.html', posts=posts, s=s)
    except DataLayerError:
        return "поврежден файл с данными"


@main_blueprint.route('/post/<int:pk>')
def post_info(pk):
    data = load_json_from_file(DATA_FILE_PATH)
    logging.info("запрошена страничка с постом")
    return render_template('post.html', post='pk')


@main_blueprint.route('/user-feed/<int:poster_name>')
def user_feed(poster_name):
    data = load_json_from_file(DATA_FILE_PATH)
    logging.info("запрошена страничка с пользователем")
    return render_template('user-feed.html', post='poster_name')


@main_blueprint.route('/bookmarks/<int:id>')
def bookmarks():
    data = load_json_from_file(DATA_FILE_PATH)
    logging.info("запрошена страничка с bookmarks")
    return render_template('bookmarks.html')
