import json
from pathlib import Path
from os.path import dirname, abspath


class UtilsDAO:
    
    def __init__(self):
        self.full_path = dirname(dirname(abspath(__file__)))+"/CW2"


    def get_posts_all(self):
        '''возвращает посты'''
        try:
            with open(self.full_path+"/static/"+'data.json', 'r', encoding='utf-8') as file:
                data = json.load(file)
            return data
        except FileNotFoundError:
            return 'File not found'
        except json.JSONDecodeError:
            return "JSON-file not decode"
        except UnicodeDecodeError:
            return "Unicode decoding problems"

    def get_posts_by_user(self, user_name):
        '''возвращает все посты пользователя по имени'''
        data = self.get_posts_all()
        return [post for post in data if user_name.lower() == post["poster_name"].lower()]

    

    def get_post_by_pk(self, pk):
        '''возвращает один пост по его идентификатору'''
        data = self.get_posts_all()
        for post in data:
            if post['pk'] == pk:
                return post
        return None
            
    def get_comments_by_post_id(self, post_id):
        '''возвращает комментарии определенного поста'''
        try:
            with open(self.full_path+"/static/"+'comments.json', 'r', encoding='utf-8') as file:
                comments = json.load(file)
            return [comment for comment in comments if int(post_id) == int(comment['post_id'])]
        except FileNotFoundError:
            return 'File not found'
        except json.JSONDecodeError:
            return "JSON-file not decode"
        except UnicodeDecodeError:
            return "Unicode decoding problems"
            
    def search_for_posts(self, query):
        '''возвращает список постов по ключевому слову'''
        data = self.get_posts_all()
        query_posts = [post for post in data if query.lower() in post['content'].lower()]
        for post in query_posts:
            post['content'] = f"{post['content'][0:50]}..."
        return query_posts

    def get_short_content_posts(self):
        '''возвращает посты с укороченным описанием'''
        data = self.get_posts_all()
        for post in data:
            post['content'] = f"{post['content'][0:50]}..."
        return data
