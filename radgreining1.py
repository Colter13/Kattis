disagree = False

length, sections = map(int, input().split())
array = ['?'] * length
for i in range(sections):
    start, sequence = input().split()
    start = int(start) - 1
    for i, ch in enumerate(sequence):
        if array[start + i] not in [ch, '?']:
            disagree = True
            break
        else:
            array[start + i] = ch
if disagree:
    print("Villa")
else:
    print(''.join(array))
