import flask
from flask import jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route("/", methods=["GET"])
def main():
    res = {
        "status_code": 200,
        "message": "hello world",
    }
    return jsonify(res)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
