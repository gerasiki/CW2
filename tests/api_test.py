from app import app


def test_get_posts_list():
    response = app.test_client().get('/api/posts/')

    assert isinstance(response.json, list)


def test_get_post_by_post_pk():
    response = app.test_client().get('/api/posts/1')

    assert isinstance(response.json, dict)


def test_check_keys_success():
    response = app.test_client().get('/api/posts/1')

    for key in ["poster_name",
                "poster_avatar",
                "pic",
                "content",
                "views_count",
                "likes_count",
                "pk"]:
        assert key in response.json.keys()


def test_check_keys_unsuccess():
    response = app.test_client().get('/api/posts/1')

    for key in ["такого ключа нет"]:
        assert not key in response.json.keys()
