class Car(): 
    """Uma Classe representando um carro"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0


    def get_descriptive_name(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        print("Este carro tem " + str(self.odometer_reading) + " de Kilometragem.")

    """Metodo usado para incrementar variavel odometer_reading"""  

    def update_odometer(self, updatekm):
        if updatekm >= self.odometer_reading: # Validando valores para não inserir valores menores que já existem
            self.odometer_reading += updatekm
        else:
            print("ATENCAO: Não é possível reduzir o odometro")

    def increment_odometer(self, km):
        self.odometer_reading += km

class Bateria():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("Este carro tem " + str(self.battery_size) + " kWh de Bateria")

    def get_range(self):
        """Exibe uma frase sobre a distancia que o carro é capaz de percorrer com essa bateria"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        mensagem = "Este carro pode roder aproximadamente " + str(range)
        mensagem += " km com carga total"
        print(mensagem)


# Criando a herança de Classe
class CarroEletrico(Car): # Chamando a Classe pai Car
    def __init__(self, make, model, year):
        super().__init__(make, model, year) # Funcao especial que cria conexoes entre a classe pai e filho  
        self.bateria = Bateria() # Aqui utilizamos a Classe Bateria como Atributo da Classe CarroEletrico
    

# Instanciamento da Classe Car para a variavel my_new_car
my_tesla = CarroEletrico('Tesla', 'model S', '2022')

# Imprimindo os dados do carro
print("\nDescricao do carro: %s" %my_tesla.get_descriptive_name()) # Outra forma de declarar variáveis

# Lendo o odometro
my_tesla.read_odometer()

# Incrementando 1800 KM no Carro
my_tesla.increment_odometer(1800)

# Odometro após o incremento de 1800
print("\nNova Kilometragem após inserir 1800 KM no odômetro")
my_tesla.read_odometer()

# Tentantiva de alterar o odomentro para 100 Kilometros no carro
print("\nTentativa de atualizar o KM no odômetro")
my_tesla.update_odometer(100)

# Atualizando o odometro inserindo mais 100 KM
print("\nNova Kilometragem após novo incremente no odômetro")
my_tesla.increment_odometer(100)
my_tesla.read_odometer()

print("\nMostrando a quantidade de bateria")
my_tesla.bateria.describe_battery()

my_tesla.bateria.get_range()