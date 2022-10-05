""" Laço While e a primeira função """
from locale import locale_alias
import random # Primeiro import de uma classe externa chamada randon (Solicita um número aleatório)

numero = 0

# Laço While que faz uma contagem até 11
while numero <= 10: # Enquanto variável número for menor que 10...
    numero += 1 # ...Some + 1 a variável número
    print(numero)

# While que solicita um numero qualquer até chegar no 1000.000 ou 812 (entra no id e aborta com o break)
while numero <= 100000:
    numero_somar = input("\nDigite um numero para somar: ")
    numero += int(numero_somar) # Convertendo o numero_somar para inteiro. Soma e insere dentro da variavel numero 
    print("\nO numero recebido é: %s" %numero) # Uma forma de declarar as variaveis em print
    if numero == 812: # Se o número for igual (==) a 812 imprima a mensagem e saia do if
        print("Você acertou o número, saindo...")
        break # Encerra o laço se cair no if com o numero 812


# Funcão que solicita um número qualquer até adivinhar
def adivinha_numero(number): # Funcao recebe o parametro number
    print("O primeiro número da tentativa é: " + str(number))
    x = random.randint(1,10) # Utiliza o metodo random importado e escolhe um numero aleatorio de 1 a 10
    while x != int(number): # Enquando a variável x (logo acima) for diferente da variavel number, rode o loop while
        number = input("\nDigite um numero para adivinhar: ") # Solicita um numero do usuario atraves do metodo input

# Chamando a função adivinha numero e passando um parametro, numero 8
adivinha_numero(8) # Chamada da função passando como Parametro o número 8



