n, m = map(int, input().split())

read = {i: 0 for i in range(1, n+1)}
unseen = 0
for i in range(1, m+1): # i represents the number of messages that have been sent
    unseen += n
    author = int(input())
    unseen -= i - read[author]
    read[author] = i
    print(unseen)