""" Laço While e a primeira função """
from locale import locale_alias
import random # Primeiro import de uma classe externa

numero = 0

# Laço While que faz uma contagem até 11
while numero <= 10:
    numero += 1
    print(numero)

# While que solicita um numero qualquer até chegar no 1000.000 ou 812
while numero <= 100000:
    numero_somar = input("\nDigite um numero para somar: ")
    numero += int(numero_somar) # Convertendo o numero_somar para inteiro. Soma e insere dentro da variavel numero 
    print("\nO numero recebido é: %s" %numero) # Uma forma de declarar as variaveis em print
    if numero == 812:
        print("Você acertou o número, saindo...")
        break # Encerra o laço se cair no if com o numero 812


# Funcão que solicita um número qualquer até adivinhar
def adivinha_numero(number):
    print("O primeiro número da tentativa é: " + str(number))
    x = random.randint(1,10)
    while x != int(number):
        number = input("\nDigite um numero para adivinhar: ")

# Chamando a função adivinha numero e passando um parametro, numero 8
adivinha_numero(8) # Parametro



