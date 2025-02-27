# Standard libs.
import os

# Dependencies through PIP.
from dotenv import dotenv_values
from flask import Flask, render_template
from flask_cors import CORS
from jinja2 import TemplateNotFound

# Local modules.
from .post_info import PostJson


# Load .env varibles
config = dotenv_values(".env")

# Store the template (post) files outside of the PIP package \
# for ease of access to posts.
TEMPLATE_DIR = os.path.abspath("./templates/")

# Same for the static files, where thumbnail images are stored.
STATIC_DIR = os.path.abspath("./static/")

# Allowed origins for Cross-Origin-Resource-Sharing
CORS_ORIGINS = config["CORS_ORIGINS"]


def create_app():
    app = Flask(
        __name__,
        static_url_path="",
        static_folder=STATIC_DIR,
        template_folder=TEMPLATE_DIR
    )

    # Enable Cross-Origin-Resource-Sharing
    CORS(app, origins=CORS_ORIGINS)

    @app.errorhandler(404)
    def not_found(error):
        return render_template("error.html"), 404

    @app.route("/blog/posts/<post>")
    def post(post):
        # Convert dash-case string from url to snake_case for filename.
        post = post.replace("-", "_")

        try:
            return render_template(f"{post}.html")
        except TemplateNotFound:

            # Replace the initial dash-replacement for a whitespace instead \
            # for prettier rendering on the client.
            post = post.replace("_", " ")

            return render_template("error.html", post_name=f"{post}")

    @app.route("/blog/all_posts")
    def all_posts():
        """
        Return all wanted meta-data from each post in the template directory.
        """

        # Make list of all the FILES in the set template directory.
        files = os.listdir(TEMPLATE_DIR)

        # Sift out all the non-post template files.
        posts = [
            os.path.join(TEMPLATE_DIR, file)
            for file in files
            if file.startswith("post")
        ]

        # Get all the raw HTML data from each post, \
        # rendering Jinja template data while at it.
        html = [render_template(os.path.basename(post)) for post in posts]

        # Find all post meta-data in each post, \
        # collecting them in a dict (json).
        json = [PostJson(data).get_json_data() for data in html]

        # 'jsonify()' runs on default with 'list' and 'dict' types in Flask. \
        # So we can simply return the dict and it will be auto-formatted.
        return json

    return app
