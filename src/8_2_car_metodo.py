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
        if updatekm >= self.odometer_reading:
            self.odometer_reading += updatekm
        else:
            print("ATENCAO: Não é possível reduzir o odometro")

    def increment_odometer(self, km):
        self.odometer_reading += km


# Instanciamento da Classe Car para a variavel my_new_car
my_new_car = Car('nivus', 'highline', '2021')

# Imprimindo os dados do carro
print("\nDescricao do carro: " + my_new_car.get_descriptive_name())

# Lendo o odometro
my_new_car.read_odometer()

# Incrementando 1800 KM no Carro
my_new_car.increment_odometer(30)

# Odometro após o incremento de 30 KM
print("\nNova Kilometragem após inserir 30 KM no odômetro")
my_new_car.read_odometer()

# Tentantiva de alterar o odomentro para 100 Kilometros no carro
print("\nTentativa de atualizar o KM no odômetro")
my_new_car.update_odometer(10)

# Atualizando o odometro inserindo mais 100 KM
print("\nNova Kilometragem após novo incremente no odômetro")
my_new_car.increment_odometer(100)
my_new_car.read_odometer()