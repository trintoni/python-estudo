"""Um pouco de FOR e LISTAS

1 - Identação
2 - Percorrendo uma lista
3 - Estutura FOR
4 - Funcao LIST
"""


carros = ['monza', 'landal', 'uno', 'gol']
for x in carros:
        print(x)

for valor in range(0,6): # Metodo range() criara uma sequencia de 1 até 5
    print(valor)



num_quadrado = [] # Definindo uma lista vazia

for value in range(1,11):
    quadrado  = value**2 # Calculado os dados ao quadrado
    num_quadrado.append(quadrado) # O metodo append() insere os novos dados calculados na lista
 
print(num_quadrado)

print("\nImprimindo o numero menor e maior") # Metodo Min e Max, imprime o maior e o menor item da Lista
print(min(num_quadrado))
print(max(num_quadrado))

#List Comprehension
# Expressao FOR acima feita em uma linha
# A Expressao nesse caso e o value**2, e o for executara isso
print("\nGerando uma lista com List Comprehensions")
quadrado = [value**2 for value in range(1,11)]
print(quadrado)


