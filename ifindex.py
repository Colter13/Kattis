s = input()

if 'i' not in s:
    print(-1)
    exit()

depths = []
depth = 0
i = 0
while i < len(s):
    if s[i]=='i':
        i += 2
        depths.append(depth)
    elif s[i]=='{':
        i += 1
        depth += 1
    else:
        i += 1
        depth -= 1

mid = len(depths) // 2
print(depths)
print(sorted(depths)[mid])