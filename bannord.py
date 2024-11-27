# Input
forbidden = set(input())
message = list(input().split())

for i, word in enumerate(message):
    if set(word) & forbidden: 
        message[i] = '*' * len(word)

print(*message)
