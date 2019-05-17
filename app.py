from flask import Flask, jsonify
from flask_cors import CORS

from access_redis import read_redis
from process_message import seperate_sentence


DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/summarization', methods=['GET'])
def summarization():
    message_list = read_redis()
    wordcloud_data = seperate_sentence(message_list)
    return jsonify(wordcloud_data)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
