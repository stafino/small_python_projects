# imported time module for test cases
import timeit

# Variable assignment
house_length = 60  # in metres
house_width = 43  # in metres
house_height = 22  # in metres

number_of_houses_in_neighbourhood = 425  # how many houses are in the given neighbourhood

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
        house_volume = house_length * house_width * house_height  # calculate the volume of the given cuboid
        neighbourhood_area = house_length * house_width * number_of_houses_in_neighbourhood  # for some different project we just want to see what's the foundations area of all houses in the given neighbourhood

with CodeTimer('CSE used - 20_000 cases'):
    for i in range(20_000):
        temporary_value = house_length * house_width  # base of the cuboid
        house_volume = temporary_value * house_height
        neighbourhood_area = temporary_value * number_of_houses_in_neighbourhood

print("----------------------------------------------------------------------")

with CodeTimer('No CSE used - 20 million cases'):
    for i in range(20_000_000):
        house_volume = house_length * house_width * house_height
        neighbourhood_area = house_length * house_width * number_of_houses_in_neighbourhood

with CodeTimer('CSE used - 20 million cases'):
    for i in range(20_000_000):
        temporary_value = house_length * house_width
        house_volume = temporary_value * house_height
        neighbourhood_area = temporary_value * number_of_houses_in_neighbourhood