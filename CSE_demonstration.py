# imported time module for test cases
import timeit

# Variable assignment
house_length = 60  # in metres
house_width = 43  # in metres
house_height = 22  # in metres
number_of_cars = 13  # how many cars we have available in the moment
number_of_houses_in_neighbourhood = 425  # how many houses are in the given neighbourhood
car_capacity = 5_000  # what's the maximum material one car can transport - in metres^3

class CodeTimer:
    def __init__(self, name=None):
        self.name = " '" + name + "'" if name else ''

    def __enter__(self):
        self.start = timeit.default_timer()

    def __exit__(self, exc_type, exc_value, traceback):
        self.took = (timeit.default_timer() - self.start) * 1000.0
        print('Code block' + self.name + ' took: ' + str(self.took) + ' ms')


print("----------------------------------------------------------------------")

with CodeTimer('No CSE used - 20_000 cases'):
    for i in range(20_000):
        volume_of_cuboid = house_length * house_width * house_height  # calculate the volume of the given cuboid
        total_car_loadout = number_of_cars * car_capacity  # what's the total number that all cars can take of the material
        neighbourhood_area = house_length * house_width * number_of_houses_in_neighbourhood  # for some different project we just want to see what's the foundations area of all houses in the given neighbourhood

with CodeTimer('CSE used - 20_000 cases'):
    for i in range(20_000):
        temporary_value = house_length * house_width  # base of the cuboid
        volume_of_cuboid = temporary_value * house_height
        total_car_loadout = number_of_cars * car_capacity
        neighbourhood_area = temporary_value * number_of_houses_in_neighbourhood

print("----------------------------------------------------------------------")

with CodeTimer('No CSE used - 20 million cases'):
    for i in range(20_000_000):
        volume_of_cuboid = house_length * house_width * house_height
        total_car_loadout = number_of_cars * car_capacity
        neighbourhood_area = house_length * house_width * number_of_houses_in_neighbourhood

with CodeTimer('CSE used - 20 million cases'):
    for i in range(20_000_000):
        temporary_value = house_length * house_width
        volume_of_cuboid = temporary_value * house_height
        total_car_loadout = number_of_cars * car_capacity
        neighbourhood_area = temporary_value * number_of_houses_in_neighbourhood