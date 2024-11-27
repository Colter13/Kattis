Nproblems = int(input())
teams = int(input())
problems = list(input().split())
scores = [0 for i in range(Nproblems)]
for i in range(teams):
    x = list(map(int, input().split()))
    for i in range(Nproblems):
        scores[i] += x[i]
print(problems[scores.index(max(scores))])