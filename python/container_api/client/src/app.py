import os

import flask
import requests
from flask import jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# switch betwween container mode $HOMENAME, or localhost mode
backend_url = os.environ.get("URL", "localhost")
backend_host = f"http://{backend_url}:8080"


@app.route("/", methods=["GET"])
def main():
    # make a request to our backend api
    try:
        res = requests.get(backend_host).json()
        res = {**res, "source": "client"}

    except Exception as exc:
        res = {
            "status_code": 400,
            "exc": exc,
        }

    # return the data to the webpage
    return jsonify(res)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8082)
