import networkx as nx

import save_load
from sessions import save_sessions, sessions

relations = {}
g = nx.Graph()
print("Введите ключ сессии:")
key = str(hash(input()))
save_sessions(sessions)
save_load.save('r' + key, relations)
save_load.save('g' + key, g)
