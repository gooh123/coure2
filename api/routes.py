from flask import Blueprint, jsonify, abort
import utils
import utils2


api_bp = Blueprint('api', __name__)


@api_bp.route('/posts')
def get_posts():
    posts = utils.get_posts_all()

    return jsonify(posts)


@api_bp.route('/posts/<int:post_id>')
def get_post(post_id):
    post = utils.get_post_by_pk(post_id)

    if post is None:
        return {'error': 'Пост не найден'}, 404

    return jsonify(post)

