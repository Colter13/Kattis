total, Benni = map(int, input().split())
bags = list(map(int, input().split()))
i = bags.index(Benni)
if i == 0:
    print("fyrst")
elif i == 1:
    print("naestfyrst")
else:
    print(i+1, "fyrst")
