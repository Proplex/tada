#!/usr/bin/python3.5

import cgi, cgitb, json

cgitb.enable()

print("Content-Type: application/json")
print()

arg_input = cgi.FieldStorage()['input'].value
response = 'Bounced off server: ' + str(arg_input)
print(json.JSONEncoder().encode(response))


