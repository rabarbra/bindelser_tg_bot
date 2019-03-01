# -*- coding: utf-8 -*-
from flask import Flask
from flask import request
from flask import jsonify
from flask import render_template
import json
import requests
import save_load
import networkx as nx

relations = {}
graph = nx.Graph()

TOKEN = "697195009:AAFewSfW90k_Guz18SlFFiC-9oZwygrks7s"
URL = "https://api.telegram.org/bot" + TOKEN + "/"

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
		
def get_file_url(file_id):
	url = URL + 'getFile'
	r = requests.post(url, json = {'file_id': file_id})
	file_path = r.json()['result']['file_path']
	file_url = 'https://api.telegram.org/file/bot' + TOKEN + '/' + file_path
	return(file_url)
		
def get_photo_id(chat_id):
	url = URL + 'getChat'
	r = requests.post(url, json = {'chat_id': chat_id})
	photo_id = r.json()['result']['photo']['big_file_id']
	return(photo_id)
	
def download_photo(url, username):
	photo = requests.get(url)
	file = open('static/img/avatars/' + username + '.jpg', 'wb')
	file.write(photo.content)
	file.close()
	

@app.route('/', methods = ['POST', 'GET'])
def index():
	if request.method == 'POST':
		r = request.get_json()
		
		chat_id = r['message']['chat']['id']
		#text = r['message']['text']
		username = r['message']['from']['username']
		person_id = r['message']['from']['id']
		photo_id = get_photo_id(chat_id)
		
		write_json(r)
		#if person_id in keys(sessions['ids']):
		#	key = sessions['ids'][id]['active_key']
		
		#download_photo(get_file_url(photo_id), username)
		#send_message(chat_id, text = text)
		#send_image(chat_id, 'static/img/avatars/'+username+'.jpg')
		
		return(jsonify(r))
	return render_template('index.html')

if __name__ == '__main__':
	app.run()