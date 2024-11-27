goal = list(input())
is_found = False
for i in range(1, int(input()) + 1):
    if is_found == True:
        break
    name = list(input())
    if len(name) == len(goal):
        disc = sum(name[j] != goal[j] for j in range(len(goal)))
        if disc <= 1:
            print(i)
            is_found = True
