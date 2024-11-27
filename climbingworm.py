climb, fall, height = map(int, input().split())
count = 1
position = 0
while position < height:
    position += climb
    if position >= height:
        break
    position -= fall
    count += 1
print(count)
