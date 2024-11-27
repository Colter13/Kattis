width, num_partitions = map(int, input().split())
partitions = [0] + list(map(int, input().split())) + [width]

possible_widths = set()  # Given case with no partitions

for i in range(len(partitions)):
    for j in range(i+1, len(partitions)):
        possible_widths.add(partitions[j] - partitions[i])

print(*sorted(possible_widths))