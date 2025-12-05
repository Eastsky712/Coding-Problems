from car import ElectricCar

my_telsa = ElectricCar('telsa', 'model s', 2019)

my_telsa.battery.describe_battery()
my_telsa.battery.get_range()
my_telsa.battery.upgrade_battery()
my_telsa.battery.get_range()

