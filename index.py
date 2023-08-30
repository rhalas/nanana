from flask import Flask, request
from flask_cors import CORS
from openai_utils import get_song_template, song_response_parser, make_openai_api_request

app = Flask(__name__)
CORS(app)

LINES_OF_LYRICS = 4

@app.route("/")
def index():
    return {"ok": "ok"}, 200

@app.route('/get_song',methods = ['POST'])
def get_song():
    if request.method != 'POST':
        return {}, 500
    
    post_req_json = request.get_json()
    song_theme = post_req_json["song_theme"]

    song_template = get_song_template(song_theme)
    response = make_openai_api_request(song_template)
    resp_body = song_response_parser(response)

    return resp_body, 200


