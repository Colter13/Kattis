n, q = map(int, input().split())

# index i represents the number 2*i + 1
# prime[i] == 1 means (2*i + 1) is prime
size = n // 2 + 1
prime = bytearray(b'\x01') * size

prime[0] = 0  # 1 is not prime

limit = int(n ** 0.5)

for p in range(3, limit + 1, 2):
    if prime[p // 2]:
        start = p * p
        # Only odd multiples need to be crossed out.
        prime[start // 2::p] = b'\x00' * (((size - 1 - start // 2) // p) + 1)

# Number of primes
count = 1 if n >= 2 else 0
count += sum(prime)

print(count)

for _ in range(q):
    x = int(input())

    if x == 2:
        print(1)
    elif x < 2 or x % 2 == 0:
        print(0)
    else:
        print(prime[x // 2])