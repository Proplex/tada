
// shell command to run
// mongo localhost:27017/db setup_mongo.js

db.users.save({"username":"testuser"});

db.notes.save({    
    "username":"testuser",
    "title":"test note title",
    "noteList": [
                {"text":"test text 1"},
                {"text":"test text 2"}
            ],
    "x":0,
    "y":0,
    "noteID":0,
    "color": "#ffffff"
});

db.events.save({
    "username":"testuser",
    "title":"test event title",
    "eventList": [
                {"start":"2017-10-14 12:00","end":"2017-10-14 01:00"},
                {"start":"2017-10-15 12:00","end":"2017-10-15 01:00"}            
            ],
    "eventID":0,
    "color": "#ffffff"
});


