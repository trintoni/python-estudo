""" Funcoes:
    Lambda 
    Maps
    Filter
    Classe OS e importando variáveis
"""
# Importando uma Classe (Para tratativas com o sistema operacional)
import os
# Classe subprocess para execução de comandos no SO
import subprocess

# Coletando a variavel de ambiente INPUT_CONSULURL
CONSUL_URL_BASE = os.environ.get('INPUT_CONSULURL')

print("Imprimindo variavel de ambiente CONSUL_URL_BASE: " + str(CONSUL_URL_BASE))

# rodando ls
subprocess.run(["ls", "-l"])
#rodando mkdir
subprocess.run(["mkdir", "teste"])

# Funcao Comun
preco = 1000

def calcular_imposto(preco):
    return preco * 0.3

print("Calculo do imposto: " + str(calcular_imposto(preco)))

# Funcao Lambda
calcular_imposto2 = lambda preco: preco * 0.3 
""" Funcao LAMBDA aqui, faz a mesma funcao que a funcao acima (calcular_imposto), a funcao lambda gerou a funcao calcular_imposto2, 
chamando o lambda em sequencia, atribuindo a variavel preco: o calculo preco * 0.3"""
print("Funcao LAMBDA: " + str(calcular_imposto2(preco)))


precos = [100, 500, 10, 25]

impostos = list(map(calcular_imposto2, precos)) 
"""A funcao map() pega uma lista, e aplica sobre cada um dos valores dessa lista (precos) uma funcao, no caso
uma funcao já existente, no caso, calcular_imposto2 (que é uma funcao lambda), ou diretamente uma funcao lambda como abaixo exemplificado.
Para utilizar o map é necessário passar como argumento uma funcao e uma lista, por exemplo: map(funcao, precos)"""
print("Retorno do MAP: " + str(impostos))


# Exemplo de uma funcao lambda diretamente na funcao map()
impostos1 = list(map(lambda x: x*2, precos)) # Multiplicando por 2
print("Map executando direto LAMBDA: " + str(impostos1))




#Funcao Filter
x = [1, 2, 3, 4, 5, 6, 122, 4432, 2332, 223, 11]
""" 
Esta funcão abaixo retorna todos os valores que são pares (divisiveis por 2, com sobra 0), caso for verdade retorna TRUE, 
caso falso, retorna FALSE
"""
def par(n):
        if n % 2 == 0:
            return True
        else:
            return False

""" 
O Filter depende da  funcao list, para obrigatoriamente retornar uma lista. O primeiro argumento da funcao filter é a função
que desejamos executar e o x é a lista de execucao.
**** Neste caso retornará somente os numeros pares (TRUE) vindos do filtro. ****
"""
print("Retornando valores Pares da lista x: " + str(list(filter(par, x))))


""" Abaixo na funcao exec_command, forçamos os atributos terem suas saídas de acordo com a configuração, no caso temos o atributo
commands, que obrigatoriamente tem seu retorno uma lista, devido ao list após os :, o atributo blocked, retorna um booleano com o valor
já configurado sendo TRUE, assim, toda essa execucao é retornada dentro de uma tupla com o comando -> tuple. Execute e repare a saida
que sera assim: (['teste', 'teste1'], True) - Uma tupla e dentro dela, uma lista e um Booleano com TRUE."""

nova_lista = ["THIAGO", "GERSON"]

def exec_command(qqcoisa: list, outra_coisa: bool = True) -> tuple: # PESQUISAR
    print(f"Exec Command: {CONSUL_URL_BASE}")
    return qqcoisa, outra_coisa

print(exec_command(nova_lista))

print(type(exec_command(nova_lista)))



def exec_command1(teste) -> list: # PESQUISAR
    return type(teste)



print("TIPO: " + str(exec_command1(10)))

"""FIM do capitulo 9"""
