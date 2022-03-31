from flask import render_template, Blueprint, request
import logging
import utils
from exceptions import DataLayerError

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')
logging.basicConfig(filename='basic.log', level=logging.INFO)

DATA_FILE_PATH = 'static/data/data.json'
COMMENTS_FILE_PATH = 'static/data/comments.json'


@main_blueprint.route('/')
def main_page():
    data = utils.load_json_from_file(DATA_FILE_PATH)
    logging.info("запрошена главная страничка")
    return render_template('index.html', information="content", posts=data)


@main_blueprint.route('/search', methods=['GET'])
def search_page():
    s = request.args.get('s', "")
    logging.info("Выполняется поиск")
    try:
        posts = utils.search_for_posts(s)
        return render_template('search.html', posts=posts, s=s)
    except DataLayerError:
        return "поврежден файл с данными"


@main_blueprint.route('/post/<int:pk>')
def post_info(pk):
    post = utils.get_post_by_pk(pk)
    comments = utils.get_comments_by_post_id(pk)

    logging.info("запрошена страничка с постом")

    return render_template('post.html', post=post, comments=comments)


@main_blueprint.route('/user-feed/<string:poster_name>')
def user_feed(poster_name):
    data = utils.get_posts_by_user(poster_name)

    logging.info("запрошена страничка с пользователем")

    return render_template('user-feed.html', post='poster_name', posts=data)


@main_blueprint.route('/bookmarks/<string:mark>')
def bookmarks(mark):
    return render_template('bookmarks.html', post=mark)

