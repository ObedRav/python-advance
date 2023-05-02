def infinite_sequence():
    result = 1
    while True:
        yield result
        result *= 5
        
value = infinite_sequence()

for i in range(5):
    print(next(value))