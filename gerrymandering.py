from math import floor

P, D = map(int, input().split())

total_votes = 0
total_A_wasted = 0
total_B_wasted = 0

votes = [[0, 0] for _ in range(D)]

for i in range(P):
    d, A_votes, B_votes = map(int, input().split())
    total_votes += A_votes + B_votes
    votes[d-1][0] += A_votes
    votes[d-1][1] += B_votes

for i in range(D):
    A_total = votes[i][0]
    B_total = votes[i][1]
    needed_votes = floor((A_total + B_total) / 2 + 1)
    if A_total > B_total:
        A_wasted = A_total - needed_votes
        B_wasted = B_total
        print('A', A_wasted, B_wasted)
    else:
        A_wasted = A_total
        B_wasted = B_total - needed_votes
        print('B', A_wasted, B_wasted)
    total_A_wasted += A_wasted
    total_B_wasted += B_wasted
print(abs(total_A_wasted - total_B_wasted) / total_votes)