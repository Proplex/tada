import cgi, cgitb, json, pymysql.cursors

def setup_db_connect():
	dbconn = pymysql.connect(host='localhost',
				 user='root',
				 password='defaultmysqlpassword',
				 db='db',
				 charset='utf8mb4',
				 cursorclass=pymysql.cursors.DictCursor)
#first connect to the db
def main():
	cgitb.enable()

	print("Content-Type: application/json")
	print()
	
	setup_db_connect()
	field_storage = cgi.FieldStorage()
	user = field_storage['user'].getValue()
	notes=None
	events=None
	
	try:
		with connection.cursor(pymysql.cursors.DictCursor)() as cursor:
			cmd = 'SELECT * FROM note WHERE username=%s'
			cursor.execute(cmd % (user))
			notes = cursor.fetchall()
		
			cmd = 'SELECT * FROM calendar WHERE username=%s'
			cursor.execute(cmd % (user))
			events = cursor.fetchall()
	except:
		print(json.JSONEncoder().encode({'error',"Unable to load data"}))
		return
	
	to_return = {"notes":notes,"events":events}
	
	print(json.JSONEncoder().encode(to_return))
	
if __name__ == '__main__':
	main()