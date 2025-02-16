#!.env/bin python3.12

from flask import Flask, request, jsonify
from pathlib import Path
from build_json import BuildJson

# Where the blogposts are stored.
POST_DIR = Path("./static/posts/")

app = Flask(__name__)

# For testing purpose to check if Flask serves images.
# Flask does serve images, make this route dymaic
# so that the request can get spesiffic image if it exists.
@app.route("/blog/api/BlogViewImage", methods=["GET"])
def BlogViewImage():
    if request.method == "GET":
        return """
            <p>showing some text, then image</p>
            <img src='http://localhost:5000/static/image.jpeg' width='500'>
            """

@app.route("/blog/api/AllBlogPostsData", methods=["GET"])
def BlogPostsData():
    if request.method == "GET":
        return jsonify(BuildJson(POST_DIR).json())
