import json
from time import sleep

"""Aqui irá gerar o arquivo numbers.json"""
numbers = [2, 3, 5, 7 ,11, 14]
filename = 'numbers.json'
with open(filename, 'w') as file_object:
    json.dump(numbers, file_object)

# Aqui irá fazer uma pausa de 10 segundos
sleep(10)

"""Aqui irá ler o JSON gerado, no caso o numbers.json"""
filename = 'numbers.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj)

print(numbers)


username = input("Qual seu nome?: ")
filename = 'username.json'

with open(filename, 'w') as f_obj:
    json.dump(username, f_obj)
    print("Vou me lembrar do seu nome quando voltar, " + username + "!")
