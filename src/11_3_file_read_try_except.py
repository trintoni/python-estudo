import json

"""Carrega o nome do usuario se foi armazenado anteriormente
Caso contrário, pede que o usuario forneça o nome e amrmazena essa informação"""

def get_stored_username():

    filename = 'username.json'
    
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def welcome_user():
    username = get_stored_username()
    if username:
        print("Bem vindo de volta, " + username + "!")
    else:
        username =  input("Qual é o seu nome: ")
        filename = 'username.json'
        with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
            print("Lembraremos quando você voltar, " + username + "!")

welcome_user()