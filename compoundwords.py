import sys

words = [word for line in sys.stdin for word in line.split()]
combinations = set()

for i in range(len(words)):
    for j in range(i+1, len(words)):
        if i != j:
            combinations.add(words[i] + words[j])
            combinations.add(words[j] + words[i])
print('\n'.join(sorted(combinations)))
