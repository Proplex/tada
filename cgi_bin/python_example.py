def test1():
	print('test 1')

def test2():
	print('test 2')

d = {'key1': test1, 'key2': test2}

d['key1']()
d['key2']()
