string = ''
output = 'valid'
for i in range(5):
    string += input()
index = 1
if string.index('k') % 2 == 1:
    index = 0
for i in range(index, 25, 2):
    if string[i] == 'k':
        output = 'invalid'
if sum([1 for ch in string if ch == 'k']) != 9:
    output = 'invalid'
print(output)
