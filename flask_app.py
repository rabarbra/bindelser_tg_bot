# -*- coding: utf-8 -*-
import json

import networkx as nx
from flask import Flask, jsonify, render_template, request

from bothandler import BotHandler

graph = nx.Graph()

TOKEN = ""  # fixme move to .env and use https://pypi.org/project/python-dotenv/

app = Flask(__name__)
bot = BotHandler(TOKEN)


def write_json(data, filename='answer.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

    r = request.get_json()

    chat_id = r['message']['chat']['id']
    text = r['message']['text']
    username = r['message']['from']['username']
    photo_id = bot.get_photo_id(chat_id)

    write_json(r)

    bot.download_photo(bot.get_file_url(photo_id), username)
    bot.send_message(chat_id, text=text)
    bot.send_image(chat_id, f'static/img/avatars/{username}.jpg')

    return jsonify(r)


if __name__ == '__main__':
    app.run()
