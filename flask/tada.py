from flask import Flask, render_template, request, jsonify
from flask_assets import Environment, Bundle
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__,
            template_folder='/var/www/html/tada/UI',
            static_folder='/var/www/html/tada/UI')
application = app
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

mongo = PyMongo(app)

def success(message, _id):
    return jsonify({'success': message, '_id': _id})

def error(message):
    return jsonify({'error':message})

@app.route('/')
def root():
	return render_template('index.html')


@app.route('/add_note',methods=['POST'])
def add_note(): 
    json_str  = request.get_json() # gets json sent from frontend
    json_dict = dict(json_str)    
    
    _id = str(ObjectId())
    json_dict['_id'] = _id

    try:	
        mongo.db.notes.insert_one(json_dict) #try to put json in db
    except Exception as e:
        print(e)
        return error(e)

    return success('add note successful', _id)



@app.route('/add_event',methods=['POST'])
def add_event():
    json_str  = request.get_json() # gets json sent from frontend
    json_dict = dict(json_str)
    
    _id = str(ObjectId())
    json_dict['_id'] = _id
    
    print(json_dict)

    try:	
        mongo.db.events.insert_one(json_str) #try to put json in db
    except Exception as e:
        print(e)
        return error(e)

    return success('add event succeeded', _id)


@app.route('/delete_note',methods=['POST'])
def delete_note():
    json_str  = request.get_json()
    print(json_str)	# get json of note function was called on
    json_dict = dict(json_str)    

    try:	
        _id = json_dict['_id'] #get its note ID (unique)
        mongo.db.notes.delete_many({'_id': ObjectId(_id)}) #delete note by its unique ID
    except Exception as e:
        print(e)
        return error(e)

    return success('delete note succeeded')


@app.route('/delete_event',methods=['POST'])
def delete_event():
    json_str  = request.get_json()
    print(json_str)	
    json_dict = dict(json_str)    

    try:	
        _id = json_dict['_id'] #grab unique id
        mongo.db.notes.delete_many({'_id': _id}) #delete by it
    except Exception as e:
        print(e)
        return error(e)

    return success('delete event succeeded')


@app.route('/edit_note',methods=['POST'])
def edit_note():
    json_str  = request.get_json()
    print(json_str)	
    json_dict = dict(json_str)

    try:
        _id = json_dict['_id'] #grab unique id
        mongo.db.notes.update_one({"noteID": noteID}, json_str) #update entry
    except Exception as e:
        print(e)
        return error(e)

    return success('update note succeeded')




@app.route('/edit_event',methods=['POST'])
def edit_event():
    json_str  = request.get_json()
    print(json_str)	
    json_dict = dict(json_str)

    try:	
        eventID = request['eventID'] #grab unique
        mongo.db.notes.update_one({"eventID": eventID}, json_str) #update by it
    except Exception as e:
        print(e)
        return error(e)

    return success('update event succeeded')


@app.route('/login',methods=['POST'])
def login():
    json_str  = request.get_json()
    print(json_str)	
    json_dict = dict(json_str)

    username = json_dict['username'] #get username from login
    
    notes = [note for note in mongo.db.notes .find({"username": username})]
    for note in notes:
        note['_id'] = str(note['_id'])
    
    events = [event for event in mongo.db.events.find({"username": username})]
    for event in events:
        event['_id'] = str(event['_id'])    
    
    return jsonify({"notes": notes, "events": events}) #Send em all over in one big json

if __name__ == '__main__':
    app.run()
