# Timing
import time

def timed(function):

    def wrapper(*args, **kwargs):
        before = time.time()
        value = function(*args, **kwargs)
        after = time.time()

        fname = function.__name__
        print(f'{fname} took {after-before} seconds to execute!')
        return value

    return wrapper

@timed
def my_func(x: int):
    result = 1
    for i in range(1, x):
        result *= i
    return result

my_func(90000)
