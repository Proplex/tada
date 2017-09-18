
import cgi, cgitb, json

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