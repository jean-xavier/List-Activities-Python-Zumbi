import bottle

@bottle.route('/')
def home_page():
	return 'Alô minha página Zumbi'

@bottle.route('/outra')
def test_page():
	return 'Outra página Zumbi'

bottle.debug(True)
bottle.run(host='192.168.100.11', port=8080)