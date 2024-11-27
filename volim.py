initial = int(input()) - 1
players = int(input())
questions = [input().split() for i in range(players)]

time = 210

for question in questions:
    time -= int(question[0])
    if time <= 0:
        break
    if question[1] == 'T':
        initial = (initial + 1) % 8
print(initial + 1)
