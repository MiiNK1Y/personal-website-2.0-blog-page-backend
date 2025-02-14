from flask import Flask, jsonify, request

app = Flask(__name__)


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
