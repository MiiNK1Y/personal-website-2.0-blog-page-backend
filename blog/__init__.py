# Native Python libs.
import os
from pathlib import Path

# External dependencies with PIP.
from flask import Flask, render_template

# Local modules.
from .post_info import PostJson

# The posts are collected togheter with other templates.
TEMPLATE_DIR = Path("blog/templates/")


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    @app.route("/blog/all_posts")
    def all_posts():
        t = os.listdir(TEMPLATE_DIR)
        f = [os.path.join(TEMPLATE_DIR, f) for f in t if f.startswith("post")]
        p = [PostJson(i).get_json_data() for i in f]

        return p  # 'jsonify()' runs on default with 'list' and 'dict' types in Flask.

    @app.route("/blog/posts/<post>")
    def post(post):
        return render_template(f"{post}.html")

    @app.errorhandler(404)
    def not_found(error):
        return render_template("error.html"), 404

    return app

