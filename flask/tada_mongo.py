from flask import Flask, render_template, request, jsonify
from flask_assets import Environment, Bundle
from flask_pymongo import PyMongo
from datetime import datetime

app = Flask(__name__,
	    template_folder='/tada/UI',
	    static_folder='/tada/UI')
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


def db_connect():
	app.config['db'] = 'db'
	mongo = PyMongo(app, config+prefix = 'db')
	
	

@app.route('/add_note',methods=['POST'])
def add_note():
	print(request.__dict__)
	print(request.get_json())
	connection = None	
	try:	
		connection = connect_to_db()
		result = db.notes.insert_one(request.get_json())
	except Exception as e:
	print('Add note failed')
		return error(e)
	finally:
		if connection != None:		
			connection.close()
	
	return success('add note succeeded')

		
			
			
@app.route('/add_event',methods=['POST'])
def add_event():
	print(request.__dict__)
	print(request.get_json())
	connection = None	
	try:	
		connection = connect_to_db()
		result = db.events.insert_one(request.get_json())
	except Exception as e:
	print('Add event failed')
		return error(e)
	finally:
		if connection != None:		
			connection.close()
	
	return success('add event succeeded')
	
	
@app.route('/delete_note',methods=['POST'])
def delete_note():
	print(request.__dict__)
	print(request.get_json())
	connection = None	
	try:	
		connection = connect_to_db()
		id = request['noteID']
		result = db.notes.delete_many({"noteID": id})
	except Exception as e:
	print('Delete note failed')
		return error(e)
	finally:
		if connection != None:		
			connection.close()
	
	return success('Delete note succeeded')

		
			
			
@app.route('/delete_event',methods=['POST'])
def delete_event():
	print(request.__dict__)
	print(request.get_json())
	connection = None	
	try:	
		connection = connect_to_db()
		id = request['eventID']
		result = db.events.remove_many({"eventID": id})
	except Exception as e:
	print('Delete event failed')
		return error(e)
	finally:
		if connection != None:		
			connection.close()
	
	return success('Delete event succeeded')
	
@app.route('/edit_note',methods=['POST'])
def edit_note():
	print(request.__dict__)
	print(request.get_json())
	connection = None	
	try:	
		connection = connect_to_db()
		id = request['noteID']
		result = db.notes.update_one({"noteID": id}, request.get_json())
	except Exception as e:
	print('Update note failed')
		return error(e)
	finally:
		if connection != None:		
			connection.close()
	
	return success('Update note succeeded')

		
			
			
@app.route('/edit_event',methods=['POST'])
def edit_event():
	print(request.__dict__)
	print(request.get_json())
	connection = None	
	try:	
		connection = connect_to_db()
		id = request['eventID']
		result = db.events.update_one({"eventID": id}, request.get_json())
	except Exception as e:
	print('Edit event failed')
		return error(e)
	finally:
		if connection != None:		
			connection.close()
	
	return success('Edit event succeeded')
	
	
@app.route('/login',methods=['POST'])
def login():
	print(request.get_json())
	username = request['username']
	notes = db.notes.find({"username": username})
	events = db.events.find({"username": username})
	retval = "{"notes": notes, "events": events}
	return success(retval)