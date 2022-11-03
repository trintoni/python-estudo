class Car(): # Declarando uma classe chamada Car (Inicia com a primeira letra em maíuscula, sempre)
    """Uma Classe representando um carro"""
    # Atributos da Classe
    def __init__(self, make, model, year): # Metodo construtor __init__, o primeiro parametro self é obrigatório
        self.make = make # declarando os atributos da classe
        self.model = model # Atributo
        self.year = year # Atributo
        self.odometer_reading = 10 # Atributo com um valor declarado diretamente

    # Metodos da Classe
    def get_descriptive_name(self): # Definindo um método, parametro self declarado para o metodo interagir com os atributos
        long_name = str(self.year) + " " + self.make + " " + self.model # Concatenacao para criar a variavel com string
        return long_name.title() # return, devolve a variável para ser utilizada

    def read_odometer(self): # Outro metodo
        print("Este carro tem " + str(self.odometer_reading) + " de Kilometragem.")


my_new_car = Car('nivus', 'highline', '2021') # Instacia da Classe Car criada em my_new_car
nome_do_carro = my_new_car.get_descriptive_name() # Instancia utilizando um metodo da classe chamado get_descriptive_name
my_new_car.read_odometer() # Instancia utilizando outro metodo

my_new_car.make = "Volkswagen" # Configurando diretamente um atributo da classe, não é uma melhor prática a utilização

print(my_new_car.make) # imprimindo um atributo da classe
print(nome_do_carro)