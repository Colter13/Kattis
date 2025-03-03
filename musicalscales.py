# generate scales
scales = {}
notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
step = [2, 2, 1, 2, 2, 2, 1]
for i in range(len(notes)):
    scales[notes[i]] = {notes[i]}
    idx = i
    for j in range(len(step)):
        idx = (idx + step[j]) % len(notes)
        scales[notes[i]].add(notes[idx])

# input
n = int(input())
melody = set(map(int, input().split()))
for scale in scales:
    