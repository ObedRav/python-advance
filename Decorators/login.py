def logged(function):
    """
    Overview

    The logged function is a decorator function that can be used to log the return
    values of any function that it decorates. The decorator function takes in another
    function as an argument and returns a wrapped version of that function that logs
    its return value to a log file named logfile.txt.

    Parameters

    function (function): The function to be decorated.

    Return Value

    The logged function returns a new function that is a wrapped version of the original function.

    Usage

    To use the logged decorator, first define a function that you want to log
    the return values for. Then, apply the @logged decorator to that function.

    For example, in the code given above, the add function is defined and
    then decorated with @logged as follows:

    @logged
    def add(x, y):
        return x + y

    Once the add function is decorated with @logged, any call to add will be logged to the logfile.txt file.

    Implementation

    The logged decorator function takes in another function as an argument and returns
    a wrapped version of that function that logs its return value to a log file named logfile.txt.

    The wrapped function, named wrapper, takes in any number of positional and keyword
    arguments using the *args and **kwargs syntax. The wrapped function then calls the
    original function, passing in the same arguments that were passed to the wrapper function.
    The return value of the original function is stored in the value variable.
    """
    def wrapper(*args, **kwargs):

        value = function(*args, **kwargs)
        with open('logfile.txt', 'a+') as f:
            fname = function.__name__
            f.write(f"{fname} returned value {value}\n")
        return value

    return wrapper

@logged
def add(x: int, y: int) -> float:
    """
    Parameters

    x (int or float): The first number to be added.
    y (int or float): The second number to be added.

    Return Value

    The add function returns the sum of the two input numbers.
    """
    return x + y

add(10, 20)
