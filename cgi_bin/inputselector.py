import cgi, cgitb, json, pymysql.cursors

cgitb.enable()

print("Content-Type: application/json")
print()

def setup_db_connect():
	dbconn = pymysql.connect(host='localhost',
								 user='root',
								 password='defaultmysqlpassword',
								 db='db',
								 charset='utf8mb4',
								 cursorclass=pymysql.cursors.DictCursor)
							 
def add_entry():
	format = cgi.FieldStorage()['format'].getvalue #note or calendar?
	text = cgi.FieldStorage()['text'].getvalue
	user = cgi.FieldStorage()['user'].getvalue
	if(format = note):
		try:
			with connection.cursor() as cursor:
			cmd = "INSERT INTO %s (username, text) VALUES (%s, %s)" #s's represent args
			cursor.execute(cmd, % (format, user, text)); #Args are passed in
			dbconn.commit(); #change needs to be committed
	if(format = calendar):
		date = cgi.FieldStorage()['date'].getvalue #TODO Going to have to format this so SQL is ok with it
		try:
			with connection.cursor() as cursor:
			cmd = "INSERT INTO %s (username, text, date) VALUES (%s, %s, %s)" #s's represent args
			cursor.execute(cmd, % (format, user, text, date)); #Args are passed in
			dbconn.commit(); #change needs to be committed		



def edit_entry():
	format = cgi.FieldStorage()['format'].getvalue #note or calendar?
	id = cgiFieldStorage()['id'].getvalue	#value is what will be used to figure out what to update
	try:
		with connection.cursor() as cursor:
		text = cgi.FieldStorage()['text'].global
		cmd = 'UPDATE %s SET text = %s WHERE id = %s'
		cursor.execute(cmd % (format, text, id))
		dbconn.commit()		
	except KeyError:
		pass
		
	try:
		with connection.cursor() as cursor:
			date = cgi.FieldStorage()['date'].global
			cmd = 'UPDATE %s SET date = %s WHERE id = %s'
			cursor.execute(cmd % (format, date, id))
			dbconn.commit()
		
	except KeyError:
		pass	

def delete_entry():
	format = cgi.FieldStorage()['format'].getvalue #note or calendar?
	id = cgiFieldStorage()['id'].getvalue		#value is what will be used to figure out what to drop
	try:
		with connection.cursor() as cursor:
		cmd = "DELETE FROM %s WHERE id= %s" #s's represent args
		cursor.execute(cmd, % (format, id)); #Args are passed in
		dbconn.commit(); #change needs to be committed

def return_error(message):
		print(json.JSONEncoder().encode({'error',message}))
		
#Main method starts below this comment
setup_db_connect()

type = cgi.FieldStorage()['type'].getvalue  #This queries the field storage for the raw string associated with the key

if type = 'add':
	add_entry()
	response = 'Add performed'
	print(json.JSONEncoder().encode(response))
	
if type = 'edit':
	edit_entry()
	response = 'Edit performed'
	print(json.JSONEncoder().encode(response))	

if type = 'delete':
	delete_entry()
	response = 'Delete performed'
	print(json.JSONEncoder().encode(response))				