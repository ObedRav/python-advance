def mydecorator(function):
    def wrapper(*args):
        print("I am decorating yoour function!")
        return function(*args)

    return wrapper

@mydecorator
def hello(person: str):
    return f"Hello {person}"

hello("Juan")