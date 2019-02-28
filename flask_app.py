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
		
def get_file_url(file_id):
	url = URL + 'getFile'
	r = requests.post(url, json = {'file_id': file_id})
	print(r.json())
	file_path = r.json()['result']['file_path']
	file_url = 'https://api.telegram.org/file/bot697195009:AAFewSfW90k_Guz18SlFFiC-9oZwygrks7s/' + file_path
	return(file_url)
		
def get_photo_id(chat_id):
	url = URL + 'getChat'
	r = requests.post(url, json = {'chat_id': chat_id})
	photo_id = r.json()['result']['photo']['big_file_id']
	return(photo_id)
	
def download_photo(url, username):
	photo = requests.get(url)
	file = open('static/img/avatars/'+username+'.jpg', 'wb')
	file.write(photo.content)
	file.close()
	

@app.route('/', methods = ['POST', 'GET'])
def index():
	if request.method == 'POST':
		r = request.get_json()
		
		chat_id = r['message']['chat']['id']
		text = r['message']['text']
		username = r['message']['from']['username']
		person_id = r['message']['from']['id']
		photo_id = get_photo_id(chat_id)
		
		
		
		
		
		
		
		
		
		
		
		if content_type != 'text':
			send_message(chat_id, 'Я понимаю только текстовые сообщения.')
		
		else:
		
			msg_list = msg['text'].split()
			option = msg_list[0].lower()
		
			if option[0] != '/':
				option = '/' + option
			
			params = msg_list[1:]
		
			sender = '@' + username
		
			if option in ['/start', '/info']:
				send_message(chat_id, 'Здесь будет инфо о боте.')
		
			elif option == '/add_conn':
				if params == []:
					pass
				else:
					add_at(params)
					Matr = save_load.load('test')
					mutual = []
					Matr.add_conn(sender, params, 1, mutual)
					graph_painting.paint(Matr, 'graph.png')
					save_load.save('test', Matr)
					
					#for conn in mutual:
						
				
			elif option == '/add_symp':
				add_at(params)
				Matr = save_load.load('test')
				Matr.add_conn(sender, params, 3)
				dict_conn = Matr.conn(sender)
				bot.sendMessage(chat_id, 'Взаимные симпатии: ' + ', '.join(dict_conn['mut_symp']))
				save_load.save('test', Matr)
				
			elif option == '/conn':
				Matr = save_load.load('test')
				dict_conn = Matr.conn(sender)
				bot.sendMessage(chat_id, 'Неподтверждённые связи: ' + ', '.join(dict_conn['conn']) + '\n\nПодтверждённые связи: ' + ', '.join(dict_conn['mut_conn']))
			
			elif option == '/symp':
				Matr = save_load.load('test')
				dict_conn = Matr.conn(sender)
				bot.sendMessage(chat_id, 'Невидимые симпатии: ' + ', '.join(dict_conn['symp']) + '\n\nВидимые симпатии: ' + ', '.join(dict_conn['vis_symp']) + '\n\nВзаимные симпатии: ' + ', '.join(dict_conn['mut_symp']))
			
			elif option == '/show_symp':
				add_at(params)
				Matr = save_load.load('test')
				Matr.show_symp(sender, params)
				graph_painting.paint_symp(Matr, 'graph.png')
				save_load.save('test', Matr)
				
			elif option == '/del_conn':
				add_at(params)
				Matr = save_load.load('test')
				Matr.del_conn(sender, params)
				graph_painting.paint(Matr, 'graph.png')
				save_load.save('test', Matr)
			
			elif option == '/del_symp':
				add_at(params)
				Matr = save_load.load('test')
				Matr.del_conn(sender, params)
				graph_painting.paint_symp(Matr, 'graph.png')
				save_load.save('test', Matr)
				
			elif option == '/graph':
				
				if params == []:
					photo = open('graph.png', 'rb')
					bot.sendPhoto(chat_id, photo)
					photo.close()
				
				else:
					how = params[0]
					Matr = save_load.load('test')
					graph_painting.paint(Matr, 'graph_{}.png'.format(how), how)
					photo = open('graph_{}.png'.format(how), 'rb')
					bot.sendPhoto(chat_id, photo)
					photo.close()
					
			elif option == '/matr':
				Matr = save_load.load('test')
				m = ''
				m = m + str(Matr.ind) + '\n\n'
				for st in Matr.Matr:
					m = m + str(st) + '\n'
				bot.sendMessage(chat_id, m)
				
			else:
				bot.sendMessage(chat_id, 'Я такого не понимаю.')
			
			
			
		#if person_id in keys(sessions['ids']):
		#	key = sessions['ids'][id]['active_key']
		
		#download_photo(get_file_url(photo_id), username)
		#send_message(chat_id, text = text)
		#send_image(chat_id, 'static/img/avatars/'+username+'.jpg')
		
		return(jsonify(r))
	return render_template('index.html')

if __name__ == '__main__':
	app.run()