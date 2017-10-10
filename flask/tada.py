from flask import Flask, render_template, request, jsonify
from flask_assets import Environment, Bundle
import pymysql



app = Flask(__name__,
	    template_folder='/home/tada_user/tada/UI',
	    static_folder='/home/tada_user/tada/UI')
assets = Environment(app)

js = Bundle('fullcalendar/lib/moment.min.js',
	    'fullcalendar/lib/jquery.min.js',
	    'fullcalendar/fullcalendar.js',
	    'note/note.js',
	    'layout/scripts/bootstrap.js',
	    'layout/scripts/bootstrap-datepicker.js',
	    'layout/scripts/bootstrap-datetimepicker.js',
	    'layout/scripts/jquery.backtotop.js',
	    'layout/scripts/jquery.mobilemenu.js',
	    'layout/scripts/jquery.placeholder.min.js',
	    output='gen/packed.js')
assets.register('js',js)

css = Bundle('fullcalendar/fullcalendar.css',
	     'layout/styles/layout.css',
	     'layout/styles/bootstrap.css',
	     'layout/styles/jquery-ui.css',
	     'layout/styles/bootstrap-datepicker.css',
	     'layout/styles/bootstrap-datetimepicker.css',
	     'note/note.css',
	     output='gen/packed.css')
assets.register('css',css)

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
	return render_template('index.html')

# format for these requests

# {"type": type, "username": username, "text": text, "datetime": datetime}
# type is note or event
# username is email
# text is string description
# datetime is datetime, *** supplied only for events


# add note or event
@app.route('/add',methods=['POST'])
def add():
	print(request.__dict__)
	print(request.get_json())
	connection = None	
	try:	
		connection = connect_to_db()
		input  = dict(request.get_json())		

		type     = input['type']
		username = input['username']
		text     = input['text']
		
		sql = ''
		if (type == 'note'):
			title = input['title']
			x = input['x']
			y = input['y']
			noteID = input['noteID']

			sql = "INSERT INTO %s (username, title, text, x, y, noteID) VALUES ('%s', '%s','%s','%s','%s','%s')" % (type,username,title,text,x,y,noteID)
		elif (type == 'event'):
			dt = input['dt']
			sql = "INSERT INTO %s (username, text, dt) VALUES ('%s', '%s', '%s')" % (type,username,text,dt)
		else:
			raise Exception()
		connection.cursor().execute(sql)
		connection.commit()
	except Exception as e:
		return error(e)
	finally:
		if connection != None:		
			connection.close()
	
	return success('add succeeded')


# edit note or event
#@app.route('/edit')
#def edit():
#	connection = None	
#	try:	
#		connection = setup_db_conn()
#		input  = request.get_json()		
#
#		type     = input['type'].getvalue
#		id       = input['id'].getvalue
#		datetime = field_storage['datetime'].getvalue
#		
#		# TODO
#		sql = 'UPDATE %s SET text = %s WHERE id = %s' % (type,text,id)
#		sql = 'UPDATE %s SET date = %s WHERE id = %s' % (type,datetime,id)
#		
#		connection.cursor().execute(sql)
#		connection.commit()
#	except:
#		return error('edit failed')
#	finally:
#		if connection != None: 
#			connection.close()
#
#	return success('edit succeeded')



# delete note or event
#@app.route('/delete')
#def delete():
#	connection = None	
#	try:	
#		connection = setup_db_conn()
#		input  = request.get_json()		
#		
#		type = input['type'].getvalue
#		id   = input['id'].getvalue	
#
#		sql = "DELETE FROM %s WHERE id = %s" % (type, id)
#
#		connection.cursor().execute(sql)
#		connection.commit()
#	except:
#		return error('delete failed')
#	finally:
#		if connection != None: 
#			connection.close()
#	return success('delete succeeded')



@app.route('/login',methods=['POST'])
def login():
	notes  = []
	events = []	
	connection = None
	try:
		connection = connect_to_db()
		with connection.cursor() as cursor:	
			input  = dict(request.get_json())

			username = input['username']

			sql = "SELECT * FROM note WHERE username = '%s'" % (username)
			cursor.execute(sql)
			notes = cursor.fetchall()
		
			sql = "SELECT * FROM event WHERE username = '%s'" % (username)
			cursor.execute(sql)
			events = cursor.fetchall()
	except Exception as e:
		return error(e)
	finally:
		if connection != None: 
			connection.close()	

	return jsonify({'notes' : notes, 'events' : events})
		
