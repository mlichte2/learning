import json

data = '''{
"name":"chuck",
"phone": {
    "type":"intl",
    "number": "+1 734 303 4456"
},
"email": {
    "hide":"yes"
}  
}'''

info = json.loads(data)
print(info)
print('name', info["name"])
print('hide', info["email"]["hide"])
