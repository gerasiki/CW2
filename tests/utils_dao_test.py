import pytest


class TestUtilsDao():

    def test_get_posts_all_is_list(self, utils_dao):
        posts = utils_dao.get_posts_all()
        assert type(posts) == list, 'Data is not a list'
        assert len(posts) > 0, 'Data is empty'

        post = posts[0]
        assert type(post) == dict, 'Items in data are not dict'

    def test_get_posts_by_user_exist(self, utils_dao):
        post_by_user_name = utils_dao.get_posts_by_user('leo')
        assert type(post_by_user_name) == list, 'Data is not a list'

    def test_get_post_by_pk_exist(self, utils_dao):
        post_1 = utils_dao.get_post_by_pk(1)
        assert type(post_1) == dict, 'Items in data are not dict'
        # assert post_1.get('poster_name') == 'leo'

    def test_get_post_by_pk_not_exist(self, utils_dao):
        post_1 = utils_dao.get_post_by_pk(-1)
        assert post_1 is None, 'Request for non existent post should return None'

    def test_get_post_by_pk_correct_keys(self, utils_dao):
        correct_keys = {'poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk'}
        post_1 = utils_dao.get_post_by_pk(1)
        post_keys = set(post_1.keys())
        assert post_keys == correct_keys, 'Incorrect set of keys'

    def test_get_comments_by_post_id(self, utils_dao):
        comments = utils_dao.get_comments_by_post_id(1)
        assert type(comments) == list, 'Data is not a list'
        assert len(comments) > 0, 'Data is empty'

        comment = comments[0]
        assert type(comment) == dict, 'Items in data are not dict'

    def test_get_comments_by_post_id_exist(self):
        pass

    def test_get_comments_by_post_id_not_exist(self):
        pass

    def test_get_comments_by_post_id_correct_keys(self, utils_dao):
        correct_keys = {"post_id", "commenter_name", "comment", "pk"}
        comments = utils_dao.get_comments_by_post_id(1)
        comment_1 = comments[0]
        comment_keys = set(comment_1.keys())
        assert comment_keys == correct_keys, 'Incorrect set of keys'

    def test_search_for_posts(self, utils_dao):
        posts_by_query = utils_dao.search_for_posts('что')
        assert type(posts_by_query) == list, 'Data is not a list'
        assert len(posts_by_query) == 6, 'Incorrect len'

    @pytest.mark.parametrize('post_pk, poster_name',
                             [
                                 (1, "leo"),
                                 (2, "johnny"),
                                 (3, "hank"),
                                 (4, "larry"),
                                 (5, "leo"),
                                 (6, "johnny"),
                                 (7, "hank"),
                                 (8, "larry")
                             ])
    def test_get_post_by_pk_value(self, utils_dao, post_pk, poster_name):
        post = utils_dao.get_post_by_pk(post_pk)
        assert post.get('poster_name') == poster_name
