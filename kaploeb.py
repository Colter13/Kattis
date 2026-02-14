input_lines, laps, contestant_number = map(int, input().split())
times = [[0, 0] for i in range(contestant_number + 1)]
     
for i in range(input_lines):
    contestant, time = input().split()
    contestant = int(contestant)
    minutes, seconds = map(int, time.split('.'))
    parsed_time = minutes*60 + seconds
    times[contestant][0] += 1
    times[contestant][1] += parsed_time

finished = []
for i in range(len(times)):
    if times[i][0] == laps:
        finished.append([i, times[i][1]])

finished.sort(key=lambda x: (x[1], x[0]))

for i in range(len(finished)):
    print(finished[i][0])