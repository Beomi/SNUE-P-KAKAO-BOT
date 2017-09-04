from flask import Flask
from flask import json, jsonify

app = Flask(__name__)


@app.route('/keyboard')
def keyboard():
    return jsonify(
        {
            "type": "buttons",
            "buttons": ["선택 1", "선택 2", "선택 3"]
        }
    )


if __name__=='__main__':
    app.run()