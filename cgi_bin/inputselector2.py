#!/usr/bin/python3.5

import cgi, cgitb, json, pymysql.cursors, os, sys

def setup_db_connect():
	global dbconn
	dbconn = pymysql.connect(host='localhost',
				 user='root',
				 password='',
				 db='db',
				 charset='utf8mb4',
				 cursorclass=pymysql.cursors.DictCursor)



def add_entry(field_storage):
	try:	
		format = field_storage['format'].getvalue # note or calendar?
		text = field_storage['text'].getvalue
		user = field_storage['user'].getvalue
		if (format == note):
			try:
				with connection.cursor() as cursor:
					cmd = "INSERT INTO %s (username, text) VALUES (%s, %s)" % (format,user,text) #s's represent args
					cursor.execute(cmd); # run it
					dbconn.commit(); #change needs to be committed
			except:
				raise Exception()
		
		if (format == calendar):
			date = field_storage['date'].getvalue #TODO Going to have to format this so SQL is ok with it
			try:
				with connection.cursor() as cursor:
					cmd = "INSERT INTO %s (username, text, date) VALUES (%s, %s, %s)"% (format, user, text, date) #s's represent args
					cursor.execute(cmd); #Run it
					dbconn.commit() #change needs to be committed
			except:
				raise Exception()
	except:
		return_error('add entry failed')
		return
	return_success('add entry success') #Need to grab the id of the new entry and send it back to the frontend

def return_success(message):
	print(json.dumps({"success":message}))

def return_error(message):
	print(json.dumps({"error":message}))


### main ###

cgitb.enable()

print("Content-Type: text/html")
print()

setup_db_connect()

global field_storage
field_storage = cgi.FieldStorage()

try:
	_type = field_storage['type'].getvalue
except:
	return_error("No type field")


dbconn.close()



