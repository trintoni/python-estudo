class Car(): 
    """Uma Classe representando um carro"""
    # Atributos da Classe
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 10

    # Metodos da Classe
    def get_descriptive_name(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        print("Este carro tem " + str(self.odometer_reading) + " de Kilometragem.")


my_new_car = Car('nivus', 'highline', '2021')
nome_do_carro = my_new_car.get_descriptive_name()
my_new_car.read_odometer()

my_new_car.make = "Volkswagen"

print(my_new_car.make)