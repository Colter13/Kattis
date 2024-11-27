n, p, x, y = map(int, input().split())

time = 0
step = 0
while p > 0:
    step += 1
    if step % n != 0:
        p -= 1
        time += x
    else:
        time += y
if (step + 1) % n == 0:
    time += y
print(time)
