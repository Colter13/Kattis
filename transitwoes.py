leaves, starts, routes = map(int, input().split())
walk_times = list(map(int, input().split()))
bus_times = list(map(int, input().split()))
bus_intervals = list(map(int, input().split()))

total_time = starts - leaves
time_elapsed = walk_times[0]

for i in range(routes):
    time_elapsed += (bus_intervals[0] - time_elapsed) % bus_intervals[0]
    time_elapsed += bus_times[i]
    time_elapsed += walk_times[i + 1]

if time_elapsed <= total_time:
    print("yes")
else:
    print("no")
