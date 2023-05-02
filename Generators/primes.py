def primes():
    yield 2
    prime_list = [2]
    n = 3
    while True:
        is_prime = True
        for p in prime_list:
            if n % p == 0:
                is_prime = False
                break
        if is_prime:
            yield n
            prime_list.append(n)
        n += 2

value = primes()


for x in range(10):
    print(next(value))
    