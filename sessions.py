# -*- coding: utf-8 -*-
import save_load

#	sessions = {
#				'ids': {
#					12312: {'username': '@rabarbrablad', 
#							 'keys': ['test', 'koto'],
#						 'active_key': 'test'},
#					45346: {'username': '@AgathaZei', 
#							 'keys': ['test', 'koto', 'poly'],
#							 'active_key': 'koto'}
#				},
#				'keys': ['test', 'koto']
#	}

def load_sessions():
	sessions = save_load.load('34r4ce')
	return(sessions)
	
def save_sessions(sessions):
	save_load.save('34r4ce', sessions)
	
def check_key(sessions, id, key):
	
	return(sessions)
	
def check_id(sessions, id, username):
	if id in keys(sessions['ids']):
		if username == sessions['ids'][id][username]:
			return(True)
		else:
			
	
def add_person():
	pass
	
