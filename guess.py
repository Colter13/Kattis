low = 1
high = 1000
mid = (low + high) // 2
while True:
    print(mid)
    response = input()
    
    if response == "lower":
        high = mid - 1
    elif response == "higher":
        low = mid + 1
    else:
        exit()
    mid = (low + high) // 2