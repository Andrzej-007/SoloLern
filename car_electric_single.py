
from car_single import Car

class ElectricCar(Car):

    def __init__(self,brand, model, year, battery_type=75):
        Car.__init__(self, brand, model, year)
        # super().__init__(brand, model, year)
        self.battery= Battery(battery_type)

class Battery():

    def __init__(self, battery_type):
        self.battery_size = battery_type

    def describe_battery(self):
        print(f'this car has battery with size : {self.battery_size} kwh')

    def get_range(self):

        if self.battery_size == 75:
            range_km = 260
        elif self.battery_size > 75:
            range_km = 315

        print(f'this  car range is approximetelly : {range_km}')