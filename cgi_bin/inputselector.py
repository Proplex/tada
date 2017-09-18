
import cgi, cgitb, json

cgitb.enable()

print("Content-Type: application/json")
print()

type = cgi.FieldStorage()['type'].value  #Comes in dict-form- this is querying the dict for the type- can be done for all fields

if type = 'add':
	response = 'Add request recieved'
	print(json.JSONEncoder().encode(response)) #This can be anything really, calling other processes etc.
	
if type = 'edit':
	response = 'Edit request recieved'
	print(json.JSONEncoder().encode(response))	

if type = 'delete':
	response = 'Delete request recieved'
	print(json.JSONEncoder().encode(response))