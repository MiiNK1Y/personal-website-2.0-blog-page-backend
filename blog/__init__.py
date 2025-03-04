# Standard libs.
import os, json

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
# Load the list from the .env as a single string \
# then convert it to a list with json.
CORS_ORIGINS = json.loads(config["CORS_ORIGINS"])


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
        """
        Returns HTML markup for an error-message for the requesting client.
        """

        return render_template("error.html"), 404

    @app.route("/blog/posts/<post>")
    def post(post):
        """
        Returns HTML markup for a single post from the Jinja tamplate directory.

        Example: /blog/posts/some-post-with-dashes

        The route uses parameter "post", in which the name of the wanted post is placed.
        The name of the post uses dashes ("-") in place of whitespaces.
        """

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
        Returns all relevant meta-data from each blog-post in the template directory in JSON format.

        If a property doesn't find a value; "None" will be used instead.

        The endpoint returns an array with the following data for each object / blog-post:

        title [str]
            Title of the post.

        tags [str]
            Tags associated with the post, each tag prefixed by a pund ("#")
            then ending with a comma before the next tag.

            Example: #here, #goes, #some, #tags

        description [str]
            A short introduction to the post or some forewords.
            Whatever relevant to introduce the theme of the post or to set the mood.

        date-of-posting [str]
            The date of which the post was published.

            Format: dd-mm-yyyy.
            Example: 31.12.2025

        date-of-last-edit [str]
            The date when the post was last edited; corrected spelling, other mistakes
            or added / removed information.

            Format: dd-mm-yyyy.
            Example: 31.12.2025

        post-url [str]
            The URL route returning the blog-post HTML markup.

            Example: https://[DOMAIN].net/blog/posts/some-post-with-dashes

        preview-img-url [str]
            The URL to the blog-post preview image.

            Example: https://[DOMAIN].net/images/some-image.png
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
