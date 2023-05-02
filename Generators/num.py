def generator(num: int):
    for i in range(num):
        yield i ** 3
        
value = generator(100)
        
for i in range(10):
    print(next(value))