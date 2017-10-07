import cgi, cgitb, json, pymysql.cursors



def setup_db_connect():
	dbconn = pymysql.connect(host='localhost',
				 user='root',
				 password='defaultmysqlpassword',
				 db='db',
				 charset='utf8mb4',
				 cursorclass=pymysql.cursors.DictCursor)


def add_entry(field_storage):
	try:	
		format = field_storage['format'].getvalue #note or calendar?
		text = field_storage['text'].getvalue
		user = field_storage['user'].getvalue
		if (format == note):
			try:
				with connection.cursor() as cursor:
					cmd = "INSERT INTO %s (username, text) VALUES (%s, %s)" % (format,user,text) #s's represent args
					cursor.execute(cmd); #Run it
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


def edit_entry(field_storage):

	try:
		format = field_storage['format'].getvalue #note or calendar?
		id = field_storage()['id'].getvalue	#value is what will be used to figure out what to update
	
		try:
			with connection.cursor() as cursor:
				text = field_storage['text'].getvalue
				cmd = "UPDATE %s SET text = %s WHERE id = %s" % (format, text, id)
				cursor.execute(cmd)
				dbconn.commit()		
		except KeyError:
			raise Exception()
		
		try:
			with connection.cursor() as cursor:
				date = field_storage['date'].getvalue
				cmd = 'UPDATE %s SET date = %s WHERE id = %s' % (format, date, id)
				cursor.execute(cmd)
				dbconn.commit()
		except KeyError:
			raise Exception()

	except:
		return_error('edit failed')
		return
	
	return_success('edit success')


def delete_entry(field_storage):
	try:
		format = field_storage['format'].getvalue
		id = field_storage['id'].getvalue	
		with connection.cursor() as cursor:
			cmd = "DELETE FROM %s WHERE id= %s" % (format, id) #s's represent args
			cursor.execute(cmd); #Run it
			dbconn.commit(); #change needs to be committed
	except:
		return_error('delete failed')


def return_error(message):
		print(json.JSONEncoder().encode({'error',message}))


def return_success(message):
		print(json.JSONEncoder().encode({'success',message}))


def main():
	cgitb.enable()

	print("Content-Type: application/json")
	print()

	setup_db_connect()
	
	field_storage = cgi.FieldStorage()

	_type = field_storage['type'].getvalue  #This queries the field storage for the raw string associated with the key

	if _type == 'add':
		add_entry(field_storage)
	
	if _type == 'edit':
		edit_entry(field_storage)

	if _type == 'delete':
		delete_entry(field_storage)
	
	dbconn.close()

if __name__ == '__main__':
	main()
