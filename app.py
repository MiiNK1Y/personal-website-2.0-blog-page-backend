#!./.env/bin/python3.12

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/api/BlogViewImage", methods=["GET"])
def BlogViewImage():
    if request.method == "GET":
        return """
            <p>showing some text, then image</p>
            <img src='http://localhost:5000/static/image.jpeg' width='500'>
            """

@app.route("/api/AllBlogPosts", methods=["GET"])
def AllBlogPosts():
    if request.method == "GET":
        return """
            <p>Here, we are going to compose all<br>blog posts found on the server!</p>
            """

@app.route("/api/AllBlogPostsData", methods=["GET"])
def BlogPostsData():
    if request.method == "GET":
        return jsonify({"some": "data", "goes": "here"})
