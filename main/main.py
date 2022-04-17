from flask import render_template, request, Blueprint
from utils_dao import UtilsDAO

main = Blueprint('main', __name__, template_folder='templates')
utils = UtilsDAO()

@main.route("/")
def page_index():
    posts = utils.get_short_content_posts()
    return render_template("index.html", posts=posts, posts_len=len(posts))


@main.route("/posts/<int:postid>")
def post_comment(postid):
    post = utils.get_post_by_pk(postid)
    comments = utils.get_comments_by_post_id(postid)
    return render_template('post.html', post=post, comments=comments, comments_len=len(comments))
    

@main.route("/search/")
def search_posts():
    search = request.args['s']
    posts = utils.search_for_posts(search)
    return render_template('search.html', search=search, posts=posts, len_posts=len(posts))


@main.route("/users/<username>")
def user_posts(username):
    posts = utils.get_posts_by_user(username)
    return render_template('user-feed.html', posts=posts)



