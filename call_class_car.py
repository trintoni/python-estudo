""" Importando e chamando Classes"""

# Importando a classe car_class_import e suas c
from car_class_import import Car, CarroEletrico


my_new_car = Car('nivus', 'highline', '2021')
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

my_electric_car = CarroEletrico('Tesla', 'Model X', '2022')
print(my_electric_car.get_descriptive_name())
print(my_electric_car.describe_battery())