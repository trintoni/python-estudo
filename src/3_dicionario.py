"""
Dicionarios (Chave: Valor) o famoso KV - Key Value

- São mutáveis, é possível excluir, adicionar (append), deletar itens, iterar

"""

usuario = {'nome': 'Anderson', 'idade': 40, 'altura': 1.74, 'nacionalidade': 'Brasileiro'} # Definindo um dicionário

print(usuario) 
print(usuario['nome']) # Imprimindo o dicionário, pegando a chave "nome", retornando o valor, "Anderson"

usuario['peso'] = "110 Kg" # Adicionando uma chave valor (KV) ao dicionario

print(usuario)

usuario['nome'] = "Hugo" # Adicionando um novo nome ao "Chave" Nome com conteúdo "Hugo"


# Este IF abaixo, substituirá o dicionário como todo, tirando "Anderson" e inserindo Hugo com o Dados 
if usuario['nome'] == 'Hugo': # Caso (if) a varivel usuario com a chave nome for igual (==) Hugo, execute... 
    usuario['peso'] = '80 Kg' # Chave peso, para valor 80 kg
    usuario['altura'] = 1.82 # Chave usuario para altura 1.82
    print(usuario)


# Aqui vemos uma outra forma de declarar um dicionário
usuario_01 = {
    'username': 'Thiago',
    'lastname': 'Barbosa',
    'matricula': 4909999999,
    'empresa': 'Via Varejo'
}

""" 
Abaixo declaramos assim:

Para as variáveis key e value, usando os dados vindos da variavel usuario1, o loop  jogará 
a chave "username" para a variável "key" e o valor "Thiago" para a varíavel value do for.
Assim, utilizará os prints para o tratamentos das variáveis já embutidas nas variáveis do loop.

"""
for key, value in usuario_01.items():
    print("\nChave: " + str(key))
    print("Valor: " + str(value) + "\n")