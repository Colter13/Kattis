start, end = map(int, input().split())

buttons = [int(input()) for _ in range(int(input()))]
travel_floors = abs(end - start)
in_between = sum(1 for floor in buttons if (start < floor < end) or (end < floor < start))
total_time = travel_floors * 4 + in_between * 10
print(total_time)
