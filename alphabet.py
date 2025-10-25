alphabet = 'abcdefghijklmnopqrstuvwxyz'
loc = {alphabet[i]: i for i in range(len(alphabet))}
s = input()
inc = [0] + [int(loc[s[i]] < loc[s[i+1]]) for i in range(1, len(s)-1)]
za = []
count = 1
for i in range(len(inc)):
    if inc[i] == 0:
        za.append(count)
        count = 1
    else:
        count += 1
za.append(count)
za = za[1:]
print(za)
print(26 - max(za))