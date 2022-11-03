"""Tuplas, são listas não mutáveis, utilizando parenteses para inicia-las"""


carros = ('Subaru', 'Nivus', 'Veloster', "Porsche", "Kombi") # Criação de uma tupla

print(type(carros)) # Monstrando o tipo do objeto, no caso uma "Tuple"

print(carros[1]) # A lista inicia seu posicionamento no 0, entao, nesse caso, mostrará: Nivus

#carros[2] = "Ferrari" # Tentando inserir dados na Tupla para gerar o Erro, descomente para testar

 
carros = ('Subaru', 'Nivus', 'Veloster', "Porsche", "Kombi", "Fusca") # Podemos sobrescrever a tupla normalmente com outros dados
carros = ('Uno') # Irá sobrescrever a lista e deixará apenas o carro Uno
print(carros)
