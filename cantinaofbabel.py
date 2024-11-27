def print_array(array):
    for i in range(len(array)):
        print(array[i])
def direct_comm(name1, name2):
    return True if speaks[names[name1]] in understands[names[name2]] else False

# Input
languages = set()
names = []
speaks = {}
understands = {}
for i in range(int(input())):
    x = input().split()
    names.append(x[0])
    speaks[x[0]] = x[1]
    understands[x[0]] = x[1:]
    for i in range(1, len(x)):
        languages.add(x[i])

# Create graph of who understands who
people = len(names)
listen = [[0] * people for _ in range(people)]
for i in range(people):
    for j in range(people):
        if speaks[names[j]] in understands[names[i]]:
            listen[i][j] = 1
