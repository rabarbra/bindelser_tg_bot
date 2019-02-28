import shelve

def save(key, obj):
	db = shelve.open('data')
	db[key] = obj
	db.close()
	
def load(key):
	db = shelve.open('data')
	obj = db[key]
	db.close()
	return(obj)

if __name__ == '__main__':
	Matr = load('test')
	print(Matr.ind)
	for st in Matr.Matr:
		print(st)