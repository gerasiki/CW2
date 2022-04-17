from flask import Blueprint, jsonify, request
from main.main import utils

api = Blueprint('api', __name__)


@api.route("/api/posts/", methods=["GET"])
def get_posts_list():
    return jsonify(utils.get_posts_all())


@api.route("/api/posts/<int:post_id>", methods=["GET"])
def get_post_dict(post_id):
    return jsonify(utils.get_post_by_pk(post_id))
