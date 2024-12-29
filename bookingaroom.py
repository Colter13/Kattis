rooms, booked = map(int, input().split())
x = [False] * rooms
for i in range(booked):
    x[int(input())] = True
if False not in x:
    print("too late")
else:
    print(x.index(False))