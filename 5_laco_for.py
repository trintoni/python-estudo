"""Um pouco de FOR e LISTAS

1 - Identação
2 - Percorrendo uma lista
3 - Estutura FOR
4 - Funcao LIST
"""


carros = ['monza', 'landal', 'uno', 'gol']
for carro in carros:
        print(carro)

for valor in range(1,5):
    print(valor)



num_quadrado = []

for value in range(1,11):
    quadrado  = value**2
    num_quadrado.append(quadrado)

print(num_quadrado)

print("\nImprimindo o numero menor e maior") # Metodo Min e Max, imprime o maior e o meno da Lista
print(min(num_quadrado))
print(max(num_quadrado))

#List Comprehension
# Expressao acima feita em uma linha
# A Expressao nesse caso e o value**2, e o for executara isso
print("\nGerando uma lista com List Comprehensions")
quadrado = [value**2 for value in range(1,11)]
print(quadrado)


