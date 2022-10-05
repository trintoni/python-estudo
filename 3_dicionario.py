"""
Dicionarios (Chave: Valor) o famoso KV - Key Value

"""

usuario = {'nome': 'Anderson', 'idade': 40, 'altura': 1.74, 'nacionalidade': 'Brasileiro'}

print(usuario)
print(usuario['nome'])

usuario['peso'] = "110 Kg"

print(usuario)

usuario['nome'] = "Hugo"


if usuario['nome'] == 'Hugo':
    usuario['peso'] = '80 Kg'
    usuario['altura'] = 1.82
    print(usuario)



usuario_01 = {
    'username': 'Thiago',
    'lastname': 'Barbosa',
    'matricula': 4909999999,
    'empresa': 'Via Varejo'
}


for key, value in usuario_01.items():
    print("\nChave: " + str(key))
    print("Valor: " + str(value) + "\n")