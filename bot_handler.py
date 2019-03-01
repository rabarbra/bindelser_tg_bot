# -*- coding: utf-8 -*-

class Bot_Handler():

	def __init__(TOKEN, chat_id):
		self.TOKEN = TOKEN
	
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