import bottle
import pymongo

#this is the handler for the default path of the web server

@bottle.route('/')
def index():

    #connect to mongoDB
    connection = pymongo.MongoClient('localhost', 27017)

    #attach to test database
    db=connection.test

    #get handler for name collection
    name= db.names #put your collection name in place of names

    #find a single document
    item=name.find_one()

    return('<b>Hello %s!<b>' %item['name']) #name your field name in place of 'names'

bottle.run(host='localhost', port=8082)

    
