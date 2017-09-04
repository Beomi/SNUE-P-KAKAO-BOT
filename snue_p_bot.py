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
            "buttons": [
                "오늘의 학식",
                "스누피 등업을 하고싶어요",
                "학교 이메일을 갖고싶어요",
                "윈도우 10을 받고싶어요"
            ]
        }
    )


@app.route('/message', methods=['POST'])
def message():
    data = request.data
    data_dict = json.loads(data)
    content = data_dict.get('content')
    if content == "오늘의 학식":
        return jsonify({
            "message": {
                'text': f'{get_menus()}'
            },
            "keyboard": {
                "type": "buttons",
                "buttons": [
                    "오늘의 학식",
                    "스누피 등업을 하고싶어요",
                    "학교 이메일을 갖고싶어요",
                    "윈도우 10을 받고싶어요"
                ]
            }
        })
    elif content == "스누피 등업을 하고싶어요":
        return jsonify({
            "message": {
                'text': '스누피 등업은 스누피 서비스에서 자동으로 할수 있어요!',
                'message_button': {
                    'label': '등업하러가기',
                    'url': 'https://service.snue-p.com/snue-p/fastverify/'
                }
            },
            "keyboard": {
                "type": "buttons",
                "buttons": [
                    "오늘의 학식",
                    "스누피 등업을 하고싶어요",
                    "학교 이메일을 갖고싶어요",
                    "윈도우 10을 받고싶어요"
                ]
            }
        })
    elif content == "학교 이메일을 갖고싶어요":
        return jsonify({
            "message": {
                'text': '학교이메일은 스누피 서비스에서 받을수 있어요!\n'
                        '원하는id@student.snue.ac.kr 주소로 만들어진답니다.\n'
                        '학교 이메일을 사용하면 구글 드라이브를 무제한으로 사용할수 있어요!',
                'message_button': {
                    'label': '학교이메일 받으러가기',
                    'url': 'https://service.snue-p.com/gapps/fastverify/'
                }
            },
            "keyboard": {
                "type": "buttons",
                "buttons": [
                    "오늘의 학식",
                    "스누피 등업을 하고싶어요",
                    "학교 이메일을 갖고싶어요",
                    "윈도우 10을 받고싶어요"
                ]
            }
        })
    elif content == "윈도우 10을 받고싶어요":
        return jsonify({
            "message": {
                'text': '윈도우 10을 받으려면 우선 학교 이메일(@student.snue.ac.kr)을 가지고 있어야 해요!\n'
                        '학교 이메일이 없다면 학교 이메일을 먼저 발급받으세요.\n'
                        '이미 학교 이메일이 있다면 아래 사이트에 학교 이메일로 가입하시고 윈 10을 무료로 받으세요!',
                'message_button': {
                    'label': '윈도 10 무료로 받기',
                    'url': 'http://snue.onthehub.com/'
                }
            },
            "keyboard": {
                "type": "buttons",
                "buttons": [
                    "오늘의 학식",
                    "스누피 등업을 하고싶어요",
                    "학교 이메일을 갖고싶어요",
                    "윈도우 10을 받고싶어요"
                ]
            }
        })


if __name__ == '__main__':
    app.run()
