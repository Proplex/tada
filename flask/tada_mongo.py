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

app.config['db'] = 'db'
mongo = PyMongo(app)


# returns a JSON dictionary where key "success" hashes to the supplied sucess message string
def success(message):
    return jsonify({'success': message})

# returns a JSON dictionary where key "error" hashes to the supplied error message string
def error(message):
    return jsonify({'error':message})


@app.route('/add_note',methods=['POST'])
def add_note():
    json_str  = request.get_json()
    print(json_str)

    try:	
        mongo.db.notes.insert_one(json_str)
    except Exception as e:
        print(e)
        return error(e)

    return success('add note succeeded')



@app.route('/add_event',methods=['POST'])
def add_event():
    json_str  = request.get_json()
    print(json_str)

    try:	
        mongo.db.events.insert_one(json_str)
    except Exception as e:
        print(e)
        return error(e)

    return success('add event succeeded')


@app.route('/delete_note',methods=['POST'])
def delete_note():
    json_str  = request.get_json()
    print(json_str)	
    json_dict = dict(json_str)    

    try:	
        noteID = json_dict['noteID']
        mongo.db.notes.delete_many({"noteID": noteID})
    except Exception as e:
        print(e)
        return error(e)

    return success('Delete note succeeded')


@app.route('/delete_event',methods=['POST'])
def delete_event():
    json_str  = request.get_json()
    print(json_str)	
    json_dict = dict(json_str)    

    try:	
        eventID = json_dict['eventID']
        mongo.db.notes.delete_many({"eventID": eventID})
    except Exception as e:
        print(e)
        return error(e)

    return success('Delete event succeeded')


@app.route('/edit_note',methods=['POST'])
def edit_note():
    json_str  = request.get_json()
    print(json_str)	
    json_dict = dict(json_str)

    try:	
        noteID = request['noteID']
        mongo.db.notes.update_one({"noteID": noteID}, json_str)
    except Exception as e:
        print(e)
        return error(e)

    return success('Update note succeeded')




@app.route('/edit_event',methods=['POST'])
def edit_event():
    json_str  = request.get_json()
    print(json_str)	
    json_dict = dict(json_str)

    try:	
        eventID = request['eventID']
        mongo.db.notes.update_one({"eventID": eventID}, json_str)
    except Exception as e:
        print(e)
        return error(e)

    return success('Update event succeeded')


@app.route('/login',methods=['POST'])
def login():
    json_str  = request.get_json()
    print(json_str)	
    json_dict = dict(json_str)

    username = json_dict['username']

    notes  = mongo.db.notes .find({"username": username})
    events = mongo.db.events.find({"username": username})

    return jsonify({"notes": notes, "events": events})

