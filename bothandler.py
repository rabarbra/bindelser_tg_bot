# -*- coding: utf-8 -*-
from typing import Union

import requests

API_TELEGRAM_HOST = 'https://api.telegram.org'
BOT_URL = f'{API_TELEGRAM_HOST}/bot'


class BotHandler:
	def __init__(self, token: str):
		self._token = token

	def url_format(self, url: str) -> str:
		"""Return full url for api call."""
		return f'{BOT_URL}/{self._token}/{url}'

	def send_message(self, chat_id: str, text: str = 'Hi') -> dict:
		url = self.url_format('sendMessage')
		request_params = {'chat_id': chat_id, 'text': text}
		response = requests.post(url, json=request_params)
		response.raise_for_status()
		return response.json()

	def send_image(self, chat_id: str, path: str) -> dict:
		url = self.url_format('sendPhoto')
		with open(path, 'rb') as photo:
			files = {'photo': photo}
			request_params = {'chat_id': chat_id}
			response = requests.post(url, files=files, data=request_params)
			response.raise_for_status()
			return response.json()

	def get_file_url(self, file_id: Union[str, int]) -> str:
		url = self.url_format('getFile')
		response = requests.post(url, json={'file_id': str(file_id)})
		response.raise_for_status()
		file_path = response.json()['result']['file_path']
		return f'{API_TELEGRAM_HOST}/file/bot/{self._token}/{file_path}'

	def get_photo_id(self, chat_id: str) -> str:
		url = self.url_format('getChat')
		response = requests.post(url, json={'chat_id': chat_id})
		response.raise_for_status()
		return response.json()['result']['photo']['big_file_id']

	@staticmethod
	def download_photo(url: str, username: str):
		photo = requests.get(url)
		with open(f'static/img/avatars/{username}.jpg', 'wb') as file:
			file.write(photo.content)
