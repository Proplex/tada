use db

db.users.save("testuser")

db.notes.save({    
    "username":"testuser",
    "title":"test note title",
    "noteList": {
                {"text":"test text 1","dt":"2017-10-14 10:00"},
                {"text":"test text 2"}            
            },
    "x":0,
    "y":0,
    "noteID":0,
    "color": "#ffffff"
})

db.events.save(
    "username":"testuser",
    "title":"test event title",
    "eventList": {
                {"dt":"2017-10-14 12:00"},
                {"dt":"2017-10-14 01:00"}            
            },
    "eventID":0,
    "color": "#ffffff"
)


