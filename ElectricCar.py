class Car:
    def __init__(self, make,model):
        self.public_make = make
        self._protected_model = model
        self.__privat_year = 2022

    def public_method(self):
        return  f'Это открытый метод.Машина:{self. public_make} ,{self._protected_model}'
    def _protected_method(self):
        return "Это защищенный метод"
    def __privat_method(self):
        return "Это приватный метод"
class ElectricCar (Car):
    def __init__(self, make, model,battery_size):
        super().__init__(make,model)
        self.battery_size = battery_size
    def get_detalis(self):
        detalis = f"{self.public_make} {self._protected_model}, Батарея:{self.battery_size}kWh"
        return detalis
tesla =ElectricCar( "Tesla","Model S","100")

print(tesla.public_make)
print(tesla.public_method())

print(tesla._protected_model)
print(tesla._protected_method())

print(tesla._Car__privat_year)