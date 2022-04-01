import pytest
from flask import Flask

from app import create_app


@pytest.fixture
def app():
    app: Flask = create_app()
    app.config['TESTING'] = True

    yield app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()


@pytest.fixture
def post_keys():
    return ["poster_name", "poster_avatar", "pic", "views_count", "likes_count", "pk", "content"]
