from flask import Flask, jsonify
import pymysql

app = Flask(__name__,
	    static_folder='/home/tada_user/tada/UI')


# support methods

# returns connection to MySQL database
def connect_to_db():
	connection = pymysql.connect(host='localhost',
				  user='root',
				  password='',
				  db='db',
				  charset='utf8mb4',
				  cursorclass=pymysql.cursors.DictCursor)
	return connection

# returns a JSON dictionary where key "success" hashes to the supplied sucess message string
def success(message):
	return jsonify({'success': message})

# returns a JSON dictionary where key "error" hashes to the supplied error message string
def error(message):
	return jsonify({'error':message})



@app.route('/')
def root():
	return app.send_static_file('index.html')

# format for these requests

# {"type": type, "username": username, "text": text, "datetime": datetime}
# type is note or event
# username is email
# text is string description
# datetime is datetime, *** supplied only for events


# add note or event
@app.route('/add')
def add():
	try:	
		connection = setup_db_conn()
		input  = request.json		
		
		type     = input['type'].getvalue
		username = input['username'].getvalue
		text     = input['text'].getvalue
		
		sql = ''
		if (type == 'note'):
			sql = 'INSERT INTO %s (username, text) VALUES (%s, %s)' % (type,username,text)
		elif (type == 'event'):
			datetime = field_storage['datetime'].getvalue
			sql = 'INSERT INTO %s (username, text, datetime) VALUES (%s, %s, %s)' % (type,username,text,datetime)
		else:
			raise Exception()
		connection.cursor().execute(sql)
		connection.commit()
	except:
		return error('add failed')
	finally:
		connection.close()
	
	return success('add succeeded')


# edit note or event
@app.route('/edit')
def edit():
	try:	
		connection = setup_db_conn()
		input  = request.json		
		
		type     = input['type'].getvalue
		id       = input['id'].getvalue
		datetime = field_storage['datetime'].getvalue
		
		# TODO
		sql = 'UPDATE %s SET text = %s WHERE id = %s' % (type,text,id)
		sql = 'UPDATE %s SET date = %s WHERE id = %s' % (type,datetime,id)
		
		connection.cursor().execute(sql)
		connection.commit()
	except:
		return error('edit failed')
	finally:
		connection.close()

	return success('edit succeeded')



# delete note or event
@app.route('/delete')
def delete():
	try:	
		connection = setup_db_conn()
		input  = request.json		
		
		type = input['type'].getvalue
		id   = input['id'].getvalue	

		sql = "DELETE FROM %s WHERE id = %s" % (type, id)

		connection.cursor().execute(sql)
		connection.commit()
	except:
		return error('delete failed')
	finally:
		connection.close()
	return success('delete succeeded')



@app.route('/login')
def login():
	notes  = []
	events = []	
	
	try:	
		connection = setup_db_conn()
		input  = request.json

		username = input['username'].getvalue

		sql = 'SELECT * FROM note WHERE username = %s' % (username)
		cursor.execute(sql)
		notes = cursor.fetchall()
		
		sql = 'SELECT * FROM calendar WHERE username = %s' % (username)
		cursor.execute(sql)
		events = cursor.fetchall()
	except:
		return error('login fetch all failed')

	return jsonify({'notes' : notes, 'events' : events})
		
