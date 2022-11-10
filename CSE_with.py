import time
import timeit
# Variable assignment
x = 1_0003_333_333
y = 3_733_591
z = 2_333_111
p = 3_231_868_844
q = 3_312_694


class CodeTimer:
    def __init__(self, name=None):
        self.name = " '"  + name + "'" if name else ''

    def __enter__(self):
        self.start = timeit.default_timer()

    def __exit__(self, exc_type, exc_value, traceback):
        self.took = (timeit.default_timer() - self.start) * 1000.0
        print('Code block' + self.name + ' took: ' + str(self.took) + ' ms')

with CodeTimer('No CSE used - 10k cases'):
   for i in range(10_000):
       a = x * y * z
       r = p * q
       b = x * y * r

with CodeTimer('CSE used - 10k cases'):
   for i in range(10_000):
       tmp_value = x * y
       a = tmp_value * z
       r = p * q
       b = tmp_value * r


with CodeTimer('No CSE used - 10 million cases'):
   for i in range(10_000_000):
       a = x * y * z
       r = p * q
       b = x * y * r

with CodeTimer('CSE used - 10 million cases'):
   for i in range(10_000_000):
       tmp_value = x * y
       a = tmp_value * z
       r = p * q
       b = tmp_value * r
