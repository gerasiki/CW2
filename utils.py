import json

PATH_POST = 'static/data.json'
PATH_COMMENT = 'static/comments.json'
__data = []


def get_posts_all():
    '''возвращает посты'''
    global __data
    try:
        with open(PATH_POST, 'r', encoding='utf-8') as file:
            __data = json.load(file)
            return __data
    except FileNotFoundError:
        return 'File not found'
    except json.JSONDecodeError:
        return "JSON-file not decode"
    except UnicodeDecodeError:
        return "Unicode decoding problems"


def get_posts_by_user(user_name):
    '''возвращает все посты пользователя по имени'''
    __data = get_posts_all()
    return [post for post in __data if user_name.lower() == post["poster_name"].lower()]


def get_comments_by_post_id(post_id):
    '''возвращает комментарии определенного поста'''
    with open(PATH_COMMENT, 'r', encoding='utf-8') as file:
        comments = json.load(file)
    return [comment for comment in comments if int(post_id) == int(comment['post_id'])]


def search_for_posts(query):
    '''возвращает список постов по ключевому слову'''
    __data = get_posts_all()
    query_posts = [post for post in __data if query.lower() in post['content'].lower()]
    for post in query_posts:
        post['content'] = f"{post['content'][0:50]}..."
    return query_posts


def get_post_by_pk(pk):
    '''возвращает один пост по его идентификатору'''
    __data = get_posts_all()
    for post in __data:
        if post['pk'] == pk:
            return post


def get_short_content_posts():
    '''возвращает посты с укороченным описанием'''
    __data = get_posts_all()
    for post in __data:
        post['content'] = f"{post['content'][0:50]}..."
    return __data

if __name__
