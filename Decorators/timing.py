# Timing
import time

def timed(function: function):
    """
    The timed decorator is a Python decorator that can be used to time the execution of a
    function. The decorator takes a single argument, which is the function to betimed.

    Parameters

    function (function): The function to be timed.

    Return Value

    The timed decorator returns a wrapped version of the input function that times the
    execution of the function and prints the execution time to the console.
    """

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
    """
    Function to test the timed decorator
    """
    result = 1
    for i in range(1, x):
        result *= i
    return result

my_func(90000)
