# Native Python libs.
import os
from pathlib import Path

# External dependencies with PIP.
from flask import Flask, render_template_string

# Local modules.
from .post_info import PostJson

# The posts are collected togheter with other templates.
# NOTE: NOT RELATIVE TO THE INSTANCE, THIS IS AN INDEPENDENT DIRECTORY.
TEMPLATE_DIR = Path("./templates/")


def create_app():
    app = Flask(__name__, template_folder=TEMPLATE_DIR)

    @app.route("/blog/all_posts")
    def all_posts():
        t = os.listdir(TEMPLATE_DIR)
        f = [os.path.join(TEMPLATE_DIR, f) for f in t if f.startswith("post")]
        p = [PostJson(i).get_json_data() for i in f]

        return p  # 'jsonify()' runs on default with 'list' and 'dict' types in Flask.

    @app.route("/blog/posts/<post>")
    def post(post):
        post = open(os.path.join(TEMPLATE_DIR, post + ".html"), "r").read()
        return render_template_string(post)

    @app.errorhandler(404)
    def not_found(error):
        error_html = open(os.path.join(TEMPLATE_DIR, "error.html"), "r").read()
        return render_template_string(error_html), 404

    return app
