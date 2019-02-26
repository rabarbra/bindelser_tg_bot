# -*- coding: utf-8 -*-
from flask import Flask
from flask import request
from flask import jsonify
from flask import render_template
import json
import requests

URL = "https://api.telegram.org/bot697195009:AAFewSfW90k_Guz18SlFFiC-9oZwygrks7s/"

app = Flask(__name__)

def write_json(data, filename = 'answer.json'):
	with open(filename, 'w') as f:
		json.dump(data, f, indent = 2, ensure_ascii = False)
		
def send_message(chat_id, text = 'Hi'):
	url = URL + 'sendMessage'
	answer = {'chat_id': chat_id, 'text': text}
	r = requests.post(url, json = answer)
	return(r.json())
	
def send_image(chat_id, path):
	url = URL + 'sendPhoto'
	with open(path, 'rb') as photo:
		files = {'photo': photo}
		data = {'chat_id': chat_id}
		r = requests.post(url, files = files, data = data)
		return(r.json())

@app.route('/', methods = ['POST', 'GET'])
def index():
	if request.method == 'POST':
		r = request.get_json()
		chat_id = r['message']['chat']['id']
		text = r['message']['text']
		send_message(chat_id, text = text)
		send_image(chat_id, 'graph.png')
		return(jsonify(r))
	return render_template('index.html')

if __name__ == '__main__':
	app.run()