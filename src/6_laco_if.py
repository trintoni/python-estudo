"""Laços IF


"""


# Uma lista de carros
carros = ['monza', 'landal', 'uno', 'gol', 'bmw', 'toyota']

for carro in carros:
    if carro == 'bmw': # Repare os dois pontos do if e o comparador de igualdade (==)
        print("Entrou no IF e modificou o bmw: " + carro.upper()) # Repare na identação do print, o metodo upper(), deixa toda string em maiúscula
    else: # Repare os dois pontos no else
        print(carro.title())




# Validando diferenças
print('\nValidando diferencas com IF')
animal = 'cachorro'

if animal != 'gato':
    print('A variavel é diferente do esperado')

print('\nTestando condicoes')
idade = 86
if idade <= 16 or idade >= 85: 
    print("Infelizmente você não pode votar")
elif idade >= 75:
    print("Você não é obrigado a votar!")
else:
    print("Vote consciente!")



recheios_disponiveis = ['tomate', 'cogumelos', 'queijo', 'calabresa', 'catupiry', 'rucula', 'oregano', 'tomate seco', 'manjericao']
recheios_solicitados = ['tomate', 'beringela', 'queijo', 'frango', 'manjericao', 'rucula', 'oregano']

print('\nPizzaria do Trinta'.upper())
for recheio_solicitado in recheios_solicitados:
    if recheio_solicitado in recheios_disponiveis:
        print("\tAdicionando recheio na pizza: " + recheio_solicitado)
    else:
        print("\tLamentamos, não temos o recheio solicitado: " + recheio_solicitado)
print("\nAssando sua pizza")