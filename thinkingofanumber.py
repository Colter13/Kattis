import math

while(True):
    n = int(input())
    if n == 0:
        exit()
    
    upper = 50001
    lower = 1
    divisors = set()
    
    for i in range(n):
        s = list(input().split())
        if s[0] == "less":
            upper = min(upper, int(s[-1]))
        elif s[0] == "greater":
            lower = max(lower, int(s[-1]) + 1)
        else:
            divisors.add(int(s[-1]))
    
    if upper == 50001:
        print("infinite")
    elif upper <= lower:
        print("none")
    else:
        if divisors:
            div = math.lcm(*divisors)
            first = div*(math.ceil(lower/div))
            valid = list(range(first, upper, div))
            if valid:
                print(*valid)
            else:
                print("none")
        else:
            print(*[i for i in range(lower, upper)])
            
    