
import cgi, cgitb, json, pymysql.cursors



cgitb.enable()

print("Content-Type: application/json")
print()

type = cgi.FieldStorage()['type'].getvalue  #This queries the field storage for the raw string associated with the key

if type = 'add':
	response = 'Add request recieved'
	print(json.JSONEncoder().encode(response)) #This can be anything really, calling other processes etc.
	
if type = 'edit':
	response = 'Edit request recieved'
	print(json.JSONEncoder().encode(response))	

if type = 'delete':
	response = 'Delete request recieved'
	print(json.JSONEncoder().encode(response))
	

def SetupDBConnect():

dbconn = pymysql.connect(host='localhost',
                             user='genericuser',
                             password='passwd',
                             db='db',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
							 
							 
	
	

def AddEntry():
format = cgi.FieldStorage()['format'].getvalue #note or calendar?
text = cgi.FieldStorage()['text'].getvalue
user = cgi.FieldStorage()['user'].getvalue
if(format = note):
	try:
		with connection.cursor() as cursor:
		cmd = "INSERT INTO %s (username, text) VALUES (%s, %s)" #s's represent args
		cursor.execute(cmd, (format, user, text)); #Args are passed in
		dbconn.commit(); #change needs to be committed
if(format = calendar):
	date = cgi.FieldStorage()['date'].getvalue #TODO Going to have to format this so SQL is ok with it
	try:
		with connection.cursor() as cursor:
		cmd = "INSERT INTO %s (username, text, date) VALUES (%s, %s, %s)" #s's represent args
		cursor.execute(cmd, (format, user, text, date)); #Args are passed in
		dbconn.commit(); #change needs to be committed		



def EditEntry():

def DeleteEntry():
	format = cgi.FieldStorage()['format'].getvalue #note or calendar?
	id = cgiFieldStorage()['id'].getvalue		#value is what will be used to figure out what to drop
	try:
		with connection.cursor() as cursor:
		cmd = "DELETE FROM %s WHERE id= %s" #s's represent args
		cursor.execute(cmd, (format, id)); #Args are passed in
		dbconn.commit(); #change needs to be committed
	