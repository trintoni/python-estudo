""" Trabalhando com variáveis em Python

Tópicos
1 - Tipos de comentários
2 - Tipos de variaveis
3 - Chamando Metodos print, upper, strip
4 - Tabulacoes em string e New Line

"""




message = "hello world" # Variavel Tipo String com aspas duplas ou simples

new_message = message.title() # Chamando um Metodo title() para deixar primeira letra Maiúscula

new_message_upper = message.upper() # Metodo upper() para deixar todas as letras em maiúscula

new_message_with_spaces = "      nome     "

number = 45 # Variavel tipo inteiro, sem aspas

name = "Anderson"  # Variavel tipo String

age = 40

var_float = 0.1 # Variavel de ponto flutuante

number_text = str(number) # Conversao de INT para STRING, somemte para essa variavel number_text


# Metodo print() imprime na saída as variáveis

print("\nIprimindo a variável message: " + message)

print("\nImprimindo a variável new_message: " + new_message)

print("\nIprimindo a variável new_message: " + new_message_upper)

print("\nIprimindo a variável new_message_with_strip: " + new_message_with_spaces)

print("\nIprimindo a variável new_message_with_strip: " + new_message_with_spaces.strip()) # Metodo strip lstrip e rstrip

print("\nImprimindo os tipos de variáveis: TIPO INT:", type(number), "TIPO FLOAT:", type(var_float))

print("\nUma soma qualquer: ", (2 + 3))

print("\nUma divisão qualquer: ", (6 / 2))

print("\nLinguagens:\n\tPython\n\tJava\n\tJavascript") # Mostrando tabulação e quebra de linha em uma string

print('\n{} is {} years old'.format(name, age)) # Utilizando o metodo Format

print(f'{name} is {age} years old') # Outra forma do metodo format


print("Teste" + str(number))


print(f'Number\t\t\tSquare\t\t\tCube') # Exemplo de format
for x in range(1, 11):
 print(f'{x:2d}\t\t\t{x*x:3d}\t\t\t{x*x*x:4d}')


"""
Guia sobre metodo format:
http://cissandbox.bentley.edu/sandbox/wp-content/uploads/2022-02-10-Documentation-on-f-strings-Updated.pdf
"""
