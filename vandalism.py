l = 'UAPC'
output = ''
s = input()
for ch in l:
    if ch not in s:
        output += ch
print(output)