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