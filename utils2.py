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
    return render_template('index.html', information="content")


@main_blueprint.route('/search')
def search_page():
    s = request.args.get('s', "")
    logging.info("Выполняется поиск")
    try:
        posts = search_for_posts(s)
        return render_template('search.html', posts=posts, s=s)
    except DataLayerError:
        return "поврежден файл с данными"


@main_blueprint.route('/post.html')
def post_info():
    data = load_json_from_file(DATA_FILE_PATH)
    user_name = "poster_name"
    content = "content"
    logging.info("запрошена страничка с постом")
    return render_template('post.html', post=content, name=user_name)


@main_blueprint.route('/user-feed.html')
def user_feed():
    data = load_json_from_file(DATA_FILE_PATH)
    logging.info("запрошена страничка с пользователем")
    return render_template('user-feed.html')


@main_blueprint.route('/bookmarks.html')
def bookmarks():
    data = load_json_from_file(DATA_FILE_PATH)
    logging.info("запрошена страничка с bookmarks")
    return render_template('bookmarks.html')
