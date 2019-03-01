import bot_handler as bot

def add_at(params):
		for l in range(len(params)):
			if params[l][0] != '@':
				params[l] = '@' + params[l]

def handle(message, relations):
	
	chat_id = message['chat']['id']
	username = '@' + message['from']['username']
	person_id = message['from']['id']
	
	try:
		text = message['text']
	except KeyError:
		
		return(None)

	if "text" not in keys(message):
				bot.send_message(chat_id, 'Я понимаю только текстовые сообщения.')
			
			else:
				
				text = message["text"]
				
				msg_list = text.split()
				option = msg_list[0].lower()
			
				if option[0] != '/':
					option = '/' + option
				
				params = msg_list[1:]
			
				sender = '@' + username
			
				if option in ['/start', '/info']:
					bot.send_message(chat_id, 'Здесь будет инфо о боте.')
			
				elif option == '/add_conn':
					if params == []:
						pass
					else:
						add_at(params)
						params = set(params)
						params.difference_update(relations[username]['mut_conn'])
						relations[username]['conn'].update(params)
						#Проверить на взаимность и отправить сообщение с подтверждениями
					
				elif option == '/add_symp':
					if params == []:
						pass
					else:
						add_at(params)
						params = set(params)
						params.difference_update(relations[username]['vis_symp'])
						relations[username]['symp'].update(set(params))
						for symp in params:
							
					
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