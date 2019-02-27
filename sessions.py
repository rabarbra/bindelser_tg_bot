# -*- coding: utf-8 -*-
import save_load

#	sessions = {
#				12312: {'username': '@rabarbrablad', 
#						 'keys': ['test', 'koto'],
#						 'active_key': 'test'},
#				45346: {'username': '@AgathaZei', 
#						 'keys': ['test', 'koto', 'poly'],
#						 'active_key': 'koto'}
#				}

def load_sessions():
	sessions = save_load.load('34r4ce')
	return(sessions)
	
def save_sessions(sessions):
	save_load.save('34r4ce', sessions)
	
def return_keys(sessions, id):
	return(sessions
	
def check_id(id, username, sessions, key):
	if id in keys(sessions) and username == sessions[id][username]
	
def add_person():
	pass
	
