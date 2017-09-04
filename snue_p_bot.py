from flask import Flask
from flask import json, jsonify
from flask import request

from cafeteria import get_menus

app = Flask(__name__)


@app.route('/', methods=['POST'])
def index():
    return 'Hello World!'


@app.route('/keyboard', methods=['GET'])
def keyboard():
    return jsonify(
        {
            "type": "buttons",
            "buttons": ["오늘의 학식보기"]
        }
    )


@app.route('/message', methods=['POST'])
def message():
    data = request.data
    data_dict = json.loads(data)
    content = data_dict.get('content')
    if content == "오늘의 학식보기":
        return jsonify({
            "message": {
                'text': f'{get_menus()}'
            },
            "keyboard": {
                "type": "buttons",
                "buttons": ["오늘의 학식보기"]
            }
        })


if __name__ == '__main__':
    app.run()
