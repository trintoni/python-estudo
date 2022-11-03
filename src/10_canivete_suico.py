compras = [
    (100, 'fone ouvido', 'usado'),
    (200, 'mouse', 'usado'),
    (5000, 'notebook', 'usado'),
    (6000, 'iphone', 'usado')
]

valor_total = 0

"""Desmebrando a tupla em duas variaveis: valor e produto"""
for valor, produto, tipo in compras:
    print(produto  + " " + tipo)

"""Neste caso, aqui, a variavel nao esta sendo utilizada, produto"""
# for valor, produto in compras:
#     valor_total += valor


"""Neste caso, aqui, a variavel nao esta sendo utilizada, produto, descartamos o dado dela com o _"""
for valor, _, _, in compras:
    valor_total = valor_total + valor

print(valor_total)




""" Comentar """

def pegar_compra(i):
    return compras[i]

_, produto, _ = pegar_compra(0)

print(produto)
