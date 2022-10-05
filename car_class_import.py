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


# Criando a herança de Classe
class CarroEletrico(Car): # Chamando a Classe pai Car
    def __init__(self, make, model, year):
        super().__init__(make, model, year) # Funcao especial que cria conecoes entre a classe pai e filho  
        self.battery_size = 70
    
    def describe_battery(self):
        print("Este carro tem " + str(self.battery_size) + " kWh de Bateria")