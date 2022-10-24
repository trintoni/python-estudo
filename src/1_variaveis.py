""" Trabalhando com variáveis em Python

Tópicos
1 - Tipos de comentários
2 - Tipos de variaveis
3 - Chamando Metodos print, upper, strip
4 - Tabulacoes em string e New Line

"""

message = "hello world" # Variavel Tipo String com aspas duplas ou simples

new_message = message.title() # Chamando um Metodo title() para deixar primeira letra Maiúscula da string

new_message_upper = message.upper() # Metodo upper() para deixar todas as letras em maiúscula da string

new_message_with_spaces = "      nome     " # Uma variavel com espaços do lado direito e esquerdo

number = 45 # Variavel tipo inteiro, sem aspas

name = "Anderson"  # Variavel tipo String, com aspas duplas

age = 40

var_float = 0.1 # Variavel de ponto flutuante

number_text = str(number) # Conversao de INTEIRO para uma STRING (str), somemte para essa variavel number_text


# Metodo print() imprime na saída as variáveis



print("\nIprimindo a variável message: " + message) # O "\n" gera uma nova linha na saída do print em tela

print("\nImprimindo a variável new_message: " + new_message) # Concatenação de string com uma variável, utilizando o "+"

print("\nIprimindo a variável new_message: " + new_message_upper)

print("\nIprimindo a variável new_message_with_strip: " + new_message_with_spaces)

print("\nIprimindo a variável new_message_with_strip: " + new_message_with_spaces.strip()) # Metodo strip lstrip e rstrip

print("\nImprimindo os tipos de variáveis: TIPO INT:", type(number), "TIPO FLOAT:", type(var_float)) # Outro tipo de concatenação de strings com vírgula

print("\nUma soma qualquer: ", (2 + 3)) # Soma diretamente na string

print("\nUma divisão qualquer: ", (6 / 2)) # Divisão

print("\nLinguagens:\n\tPython\n\tJava\n\tJavascript") # Mostrando tabulação e quebra de linha em uma string (\n - nova linha \t - tabulacao)

print('\n{} is {} years old'.format(name, age)) # Utilizando o metodo Format para mostrar as variáveis

print(f'{name} is {age} years old') # Outra forma do metodo format


print("Teste" + str(number)) # String e a conversão de um numero para string


print(f'Number\t\t\tSquare\t\t\tCube') # Exemplo de format
for x in range(1, 11):
 print(f'{x:2d}\t\t\t{x*x:3d}\t\t\t{x*x*x:4d}')


"""
Guia sobre metodo format:
http://cissandbox.bentley.edu/sandbox/wp-content/uploads/2022-02-10-Documentation-on-f-strings-Updated.pdf
"""
