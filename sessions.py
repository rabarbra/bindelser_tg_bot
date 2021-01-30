# -*- coding: utf-8 -*-
import save_load

sessions = {
    'ids': {
        12312: {'username': '@rabarbrablad', 'keys': ['test', 'koto'], 'active_key': 'test'},
        45346: {'username': '@AgathaZei', 'keys': ['test', 'koto', 'poly'], 'active_key': 'koto'}
    },
    'keys': ['test', 'koto']
}


def save_sessions(payload: dict):
    save_load.save('34r4ce', payload)
