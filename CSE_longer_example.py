# imported time module for test cases
import timeit

# our house
house_length = 60  # in metres
house_width = 43  # in metres
house_height = 22  # in metres
number_of_houses_in_neighbourhood = 425  # how many houses are in the given neighbourhood

# ping pong balls
pingpong_radius = 0.02  # radius of pingpong ball in metres
pingpong_weight = 0.003  # weight of pingpong ball in grams
volume_of_pingpong = 4 / 3 * 3.14 * pingpong_radius * pingpong_radius # 1 ping pong ball volume - Volume= 4/3*(pi)(r cubed).

# Transportation
truck_capacity = 5_000  # what's the maximum material one car can transport - in kilograms


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
        number_of_pingpongs_in_house = house_length * house_width * house_height / volume_of_pingpong  # how many ping pong balls fit in the house
        total_weight_pingpong = number_of_pingpongs_in_house * pingpong_weight
        trucks_needed = total_weight_pingpong / truck_capacity
        neighbourhood_area = house_length * house_width * number_of_houses_in_neighbourhood  # for some different project we just want to see what's the foundations area of all houses in the given neighbourhood

    print(f'Total number of all balls: {number_of_pingpongs_in_house}. Total weight of all balls: {total_weight_pingpong}. Total cars needed: {trucks_needed}')

with CodeTimer('CSE used - 20_000 cases'):
    for i in range(20_000):
        temporary_value = house_length * house_width  # base of the cuboid
        house_volume = temporary_value * house_height  # calculate the volume of the given cuboid
        number_of_pingpongs_in_house = house_volume / volume_of_pingpong  # how many ping pong balls fit in the house
        total_weight_pingpong = number_of_pingpongs_in_house * pingpong_weight
        trucks_needed = total_weight_pingpong / truck_capacity
        neighbourhood_area = temporary_value * number_of_houses_in_neighbourhood  # for some different project we just want to see what's the foundations area of all houses in the given neighbourhood



print("----------------------------------------------------------------------")

with CodeTimer('No CSE used - 20 million cases'):
    for i in range(20_000_000):
        house_volume = house_length * house_width * house_height  # calculate the volume of the given cuboid
        number_of_pingpongs_in_house = house_volume / volume_of_pingpong  # how many ping pong balls fit in the house
        total_weight_pingpong = number_of_pingpongs_in_house * pingpong_weight
        trucks_needed = total_weight_pingpong / truck_capacity

        neighbourhood_area = house_length * house_width * number_of_houses_in_neighbourhood  # for some different project we just want to see what's the foundations area of all houses in the given neighbourhood


with CodeTimer('CSE used - 20 million cases'):
    for i in range(20_000_000):
        temporary_value = house_length * house_width  # base of the cuboid
        house_volume = temporary_value * house_height  # calculate the volume of the given cuboid
        number_of_pingpongs_in_house = house_volume / volume_of_pingpong  # how many ping pong balls fit in the house
        total_weight_pingpong = number_of_pingpongs_in_house * pingpong_weight
        trucks_needed = total_weight_pingpong / truck_capacity
        neighbourhood_area = temporary_value * number_of_houses_in_neighbourhood  # for some different project we just want to see what's the foundations area of all houses in the given neighbourhood
