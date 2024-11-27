tasks, time = map(int, input().split())
task_times = list(map(int, input().split()))

time_elapsed = 0
completed_tasks = 0

for task_time in task_times:
    time_elapsed += task_time
    if time_elapsed > time:
        break
    completed_tasks += 1

print(completed_tasks)
