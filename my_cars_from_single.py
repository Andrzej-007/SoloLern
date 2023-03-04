
from car_single import Car
from car_electric_single import ElectricCar, Battery


my_beetle = Car('valksvagen', 'beetle', '2019')
print(my_beetle.get_description(),'\n')

my_melex = ElectricCar('melex', 'model_s_100', 1975, 104 )
print(my_melex.get_description())
my_melex.battery.describe_battery()
my_melex.battery.get_range()