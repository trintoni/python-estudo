""" Listas

1 - O que é uma lista

"""

bicycles = ['trek', 'redline', 'specialized', 'cannondale'] # Criando a lista com conteúdo

print("Imprimindo a lista bycicles: ")
print(bicycles) # Imprimindo a lista bicycles


print("\nImprimindo um item específico da lista: " + bicycles[0]) # Mostrando a posicao 0 da lista

print("\nImprimindo outro item específico da lista: " + bicycles[3])

print("\nImprimindo o último item específico da lista: " + bicycles[-1]) # Mostra o ultimo item de uma lista, utilizando o [-1]

print('\nMinha primera bicicleta era uma ' + bicycles[2].title()) 
print("\n")

# Interagindo com a lista

motos = ['honda', 'yamaha', 'suzuki']

print(motos)

motos[0] = 'Dafra'

print(motos)

# Acrescentando elementos no final da lista
print("\nFazendo um append de uma moto Ducatti")
motos.append('ducati') # Metodo append() utilizando para inserir dados na lista
print(motos)

motos_usadas = [] # Criando uma lista vazia

motos_usadas = ['Harley Davidson', 'Kawasaki']

motos_usadas.insert(1, 'Royal Enfield') # Insere no local informado (1) o conteúdo Royal Enfield

print("\nMotos usadas, adicionado uma Royal Enfield na posicao 1")
print(motos_usadas)

del motos_usadas[0] # Retira da posicao 0 (Harley Davidson) da lista

print("\nRetirando a posicao Harley Davidson da posicao 0")
print(motos_usadas)

motos_vendidas = motos_usadas.pop() # O metodo pop, retira o ultimo item da lista e neste caso armazena em uma variável, motos vendidas.

print("\nUtilizando o metodo POP para retirar o ultimo item da lista e armazenar em uma variavel")
print("A moto vendida foi: " + motos_vendidas)

motos.remove('ducati') # O metodo remove(), remove o item pelo nome, retira o "ducati" da lista
 
print("Lista de motos sem a Ducati: ")
print(motos)

# Metodo sort - ordenando

motos_zero_km = ['BRP', 'Bull', 'Dafra', 'Motorino', 'Voltz', 'Kymco', 'Avelloz']
print("\nImprimindo listas não ordenadas")
print(motos_zero_km)

print("\nImprimindo lista ordenadas")
motos_zero_km.sort() # Ordenando por ordem alfábetica, metodo sort()
print(motos_zero_km)

print("\nImprimindo lista em ordem reversa")
motos_zero_km.reverse() # Ordenando por ordem alfábetica pelo metodo sort() acima
print(motos_zero_km)


print("\nDescobrindo o tamanho de uma lista")
motos_zero_km.reverse() # Ordenando por ordem alfábetica, ao contrário
tamanho_lista = len(motos_zero_km) # Mostra o tamanho da lista
print("O tamanho da lista é: " + str(tamanho_lista)) # Usando o metodo str para converter a saída da lista em uma string para concatenacao


numeros = list(range(1,10)) # Criando uma lista a partir da funcao list() de 1 até 10
print("Criando uma lista a partir da funcao list")
print(numeros)

lista_numeros = list(range(1,21))
print(lista_numeros)

print("\nImprimindo os 10 primeiros números de uma lista")
print(lista_numeros[0:10]) # Imprimindo os 10 primeiros números de uma lista


print("\nCopiando uma lista")
nova_lista_numeros = lista_numeros[:] # Para copiar uma lista, utilize o [:], caso nao seja assim, apenas a referencia de variavel sera criada para a lista em questao
print(nova_lista_numeros)


