n = int(input())
votes = sorted(list(map(int, input().split())), reverse=True)
mark = sum(votes) // 2
diff = mark - votes[1]
round = 1
for i in range(n-1, 1, -1):
    diff -= votes.pop(i)
    if diff < 0:
        print(round)
        exit()
    round += 1
print("IMPOSSIBLE TO WIN")