import bottle

@bottle.route('/')
def home_page():
	mythings = ['Python', 'NodeJs', 'C++', 'PHP']
	return bottle.template('hello_world', {'username':'Jean', 'things':mythings})

bottle.debug(True)
bottle.run(host='192.168.100.11', port=8080)