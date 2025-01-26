primes = []
num = 2
while len(primes) < 100:
    flag = True
    for prime in primes:
        if prime > num:
            break
        if num % prime == 0:
            flag = False
            break
    if flag == True:
        primes.append(num)
    num += 1
print(*primes, sep='\n')