n = 12
primes = [2, 7, 13, 19]


c = 1
n = 2
while c < 12:
    print(n)
    for ele in primes:
        if n % ele == 0:
            n += 1
            c += 1
            continue
    n += 1

print(n)
