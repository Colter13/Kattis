# input
n = int(input())
colors = list(input())

# variables
ptr = 0
commands = ''
prev = -1

for i in range(n):
    distance = {
        'R': -1,
        'G': -1,
        'B': -1
    }
    for j in range(prev + 1, len(colors)):
        if colors[j] == 'R' and distance['R'] == -1:    # Isn't executing on test case 2
            distance['R'] = j+1
        elif colors[j] == 'G' and distance['G'] == -1:
            distance['G'] = j+1
        elif colors[j] == 'B' and distance['B'] == -1:
            distance['B'] = j+1
        prev = j
        if -1 not in distance.values():
            break
    commands += colors[prev]
print(commands)