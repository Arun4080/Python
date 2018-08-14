import bottle

@bottle.route('/')
def home_page():
    return("hello world \n")


@bottle.route('/testpage')
def home_page():
    return("this is test page \n")

bottle.debug(True)
bottle.run(host='localhost', port=8080)
