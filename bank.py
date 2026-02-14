n, t = map(int, input().split())

people = []

for i in range(n):
    c, t = map(int, input().split())
    people.append([c, t, False])
    
people.sort(key=lambda x: x[1])

total = 0

for currentTime in range(t - 1, -1, -1):
    bestPerson = -1
    bestCash = 0
    
    for i in range(n):
        cash, leaveTime, served = people[i]
        if not served and leaveTime >= currentTime:
            if cash > bestCash:
                bestCash = cash