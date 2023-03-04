
class Car():

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.odometer = 0

    def get_description(self):
        long_name = f'{self.brand} {self.model} {self.year}'
        return long_name.title()

    def read_odometer(self):
        print(f'this car has driven : {self.odometer}')

    def update_odometeer(self, meter):

        if meter < self.odometer:
            print(" you cant take back milage")
        else:
            self.odometer = meter

    def increment_meters(self, meter):
        self.odometer += meter


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



# my_tesla =  ElectricCar('tesla', "model s3", 2019)
# print(my_tesla.get_description())
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()