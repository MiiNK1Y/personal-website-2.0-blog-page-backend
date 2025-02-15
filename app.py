#!./.env/bin/python3.12

# NOTE:
# Current idea for implementing a backend for the blog-page:
#
# FOR THE FRONT BLOG-PAGE (WHERE ALL THE BLOGS ARE ORGANIZED)
#  - Use Flask to serve JSON with:
#       1. Title / header
#       2. Thumbnail / preview (as src links to the backend)
#       3. Tags
#       4. Introduction / TL;DR
#
# HOW TO GO ABOUT GETTING JSON DATA FROM THE MARKDOWN FILES THEMSELVES:
# TO AVOID HAVING TO MANUALLY WRITE THE JSON FILES TO BE SERVED MANUALLY?
#  - Write some code to fetch the following contents from the MD files.
#       CON:
#           - I would have to use some static MD template to make the MD file predictable for the program.
#       PRO:
#           - I can dynamically edit the files and the update on the Clinet side would be emediate.
#
# - STUFF TO KEEP IN MIND WHEN WRITING THIS:
#       1. Some system to keep up with tags on posts.
#
# PR BLOG POST (THE POSTS THEMSELVES):
#  - Use Flask to serve static HTML, allready prepared the styling on the client-side with Vue.

from flask import Flask, jsonify, request
import marko


app = Flask(__name__)


with open("./posts/post-1.md", "r") as f:
    test_text = f.read()


@app.route("/post-1", methods=["GET"])
def post_1():
    if request.method == "GET":
        data = "This is post-1!"
        return jsonify({"data": data})


@app.route("/post-2", methods=["GET"])
def post_2():
    if request.method == "GET":
        data = "This is post-2!"
        return jsonify({"data": data})

