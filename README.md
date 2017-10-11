# TaDa
Web application that is a clone of Trello and Google Calendar. On the left side, a user can create notes, and on the right, the user can add events to a calendar. 

### MVP Notes

<ul>
<li>you can only have 3 notes</li>
<li>once notes are saved you cannot edit or delete</li>
<li>once an event has been added it cannot be edited or deleted</li>
</ul>

The above features are not in the MVP, but will likely be accomplished for beta release.

# To Use the MVP (tested only on Ubuntu)

### Clone the Repo
```
git clone https://github.com/CosmicVarion/tada.git
```

### Build Docker Image

To build from the tada directory:
```
docker build -t tada_flask_image docker/
```
The Dockerfile is in the docker directory.

### Run Docker Container

To run a container based on the built image:
```
docker run --rm -it --name=tada_flask_server -p 5000:5000 tada_flask_image /bin/bash
```

### Then

Restart MySQL, source our SQL database file from the MySQL prompt, and run flask in the container:
```
service mysql restart
cd flask
mysql # to open mysql prompt
mysql> setup_db.sql # in mysql prompt
mysql> quit # to exit mysql prompt
FLASK_APP=/tada/flask/tada.py flask run --host=0.0.0.0
```

### Finally, to Use TaDa

In Chrome, go to http://localhost:5000 sign in thru Google OAUTH and use the app. Add notes to the left side, and save them with the save button. Create events on the left with the create event button.

We also apologize for making you build the container, but it was ~600 MB when saved...
