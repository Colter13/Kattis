def sum_of_digits_to_n(n):
    if n < 0:
        return 0
    sum_digits = 0
    factor = 1  # This represents the positional multiplier for each digit
    while n >= factor:
        lower_numbers = n - (n // factor) * factor
        current_digit = (n // factor) % 10
        higher_numbers = n // (factor * 10)
        
        # Sum of digits for all numbers formed by lower numbers
        sum_digits += higher_numbers * (factor * 45)
        
        # Sum of digits for numbers formed by the current digit
        sum_digits += current_digit * (lower_numbers + 1)
        
        # Sum of all digits from 1 to current_digit-1 at the current factor place
        sum_digits += (current_digit * (current_digit - 1) // 2) * factor
        
        factor *= 10

    return sum_digits

def compute_sum(start, stop):
    return sum_of_digits_to_n(stop) - sum_of_digits_to_n(start - 1)

def main():
    num_cases = int(input())
    results = []
    for _ in range(num_cases):
        start, stop = map(int, input().split())
        results.append(compute_sum(start, stop))
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
