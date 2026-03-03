from collections import defaultdict

n, k = map(int, input().split())

pref = defaultdict(list)
for i in range(n):
    _, *l = input().split()
    pref[i] = l

ranklist = []
num = int(input())
for i in range(num):
    ranklist.append(input())

taken = set()
teams = [[] for i in range(n)]
for i in range(k): #num rounds
    for j in range(n): #num managers
        added = False

        # search through preference list
        while pref[j]:
            selection = pref[j].pop(0)
            if selection not in taken:
                taken.add(selection)
                teams[j].append(selection)
                added = True
                break
        
        # choose ranklist
        if not added:
            while True:
                selection = ranklist.pop(0)
                if selection not in taken:
                    taken.add(selection)
                    teams[j].append(selection)
                    break
        
for i in range(n):
    print(*teams[i])
        
