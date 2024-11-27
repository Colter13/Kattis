days = [False] * 365
for i in range(int(input())):
    day_start, day_end = map(int, input().split())
    days[day_start-1:day_end] = [True] * (day_end - day_start + 1)
print(sum(days))
