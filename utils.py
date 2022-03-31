import json
# from pprint import pprint as pp
import logging

logging.basicConfig(filename='basic.log', level=logging.INFO)


DATA_FILE_PATH = 'static/data/data.json'
COMMENTS_FILE_PATH = 'static/data/comments.json'


def load_json_from_file(file_path):
    with open(file_path, encoding='utf8') as file:
        return json.load(file)


def get_posts_all():
    data = load_json_from_file(DATA_FILE_PATH)

    return data


def get_posts_by_user(user_name):
    data = load_json_from_file(DATA_FILE_PATH)
    user_name = user_name.lower()
    posts_found = []

    for post in data:
        if user_name.lower() in post['poster_name'].lower():
            posts_found.append(post)
    return posts_found


def get_comments_by_post_id(post_id):
    data = load_json_from_file(COMMENTS_FILE_PATH)

    result = []
    for comment in data:
        if comment['post_id'] == post_id:
            result.append(comment)

    return result


def search_for_posts(query):
    query = query.lower()
    posts_found = []

    posts = load_json_from_file(DATA_FILE_PATH)
    for post in posts:
        if query in post["content"].lower():
            posts_found.append(post)

    return posts_found


def get_post_by_pk(pk):
    data = load_json_from_file(DATA_FILE_PATH)

    found_post = None
    for post in data:
        if post['pk'] == pk:
            found_post = post
            break

    return found_post
