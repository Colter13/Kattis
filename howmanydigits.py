import sys
import math

def factorial_digit_count(n):
    if n == 0 or n == 1:
        return 1
    log_factorial = 0.5 * math.log10(2 * math.pi * n) + n * math.log10(n / math.e)
    return math.floor(log_factorial) + 1

for line in sys.stdin:
    n = int(line.strip())
    print(factorial_digit_count(n))
