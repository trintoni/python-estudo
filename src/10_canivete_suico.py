compras = [
    (100, 'fone ouvido'),
    (200, 'mouse'),
    (5000, 'notebook'),
    (6000, 'iphone')
]

valor_total = 0

"""Desmebrando a tupla em duas variaveis: valor e produto"""
for valor, produto in compras:
    print(produto)

"""Neste caso, aqui, a variavel nao esta sendo utilizada, produto"""
# for valor, produto in compras:
#     valor_total += valor


"""Neste caso, aqui, a variavel nao esta sendo utilizada, produto, descartamos o dado dela com o _"""
for valor, _ in compras:
    valor_total = valor_total + valor

print(valor_total)



def pegar_compra(i):
    return compras[i]


_, produto = pegar_compra(1)

print(produto)
