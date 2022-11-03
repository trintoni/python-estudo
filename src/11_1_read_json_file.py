import json

filename = 'username.json'
with open(filename) as file_object:
    username = json.load(file_object)
    print("Bem vindo de volta, " + username + "!")