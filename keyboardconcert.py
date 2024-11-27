# input
instruments, notes = map(int, input().split())
l = []  # temporarily variable to store notes before putting them in the dict
for i in range(instruments):
    x, *rest = map(int, input().split())
    l.append(rest)
notes = list(map(int, input().split()))

# generate dictionary for notes
keys = {note: set() for note in set(notes)}
for i in range(len(l)):
    for key in l[i]:
        keys[key].add(i)

# cycle through notes
switches = 0
curr = keys[notes[0]].copy()
for i in range(1, len(notes)):
    curr.intersection_update(keys[notes[i]])
    if len(curr) == 0:
        switches += 1
        curr = keys[notes[i]].copy()

# output
print(switches)