import networkx as nx
from sessions import save_sessions
import save_load

sessions = {}
relations = {}
g = nx.Graph()
print("Введите ключ сессии:")
key = str(hash(input()))
save_sessions(sessions)
save_load.save('r' + key, relations)
save_load.save('g' + key, g)