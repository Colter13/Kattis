lowercase = 'abcdefghijklmnopqrstuvwxyz'
uppercase = lowercase.upper()

whitespace = 0
lower = 0
upper = 0
symbols = 0

for ch in input():
    if ch == '_':
        whitespace += 1
    elif ch in lowercase:
        lower += 1
    elif ch in uppercase:
        upper += 1
    else:
        symbols += 1

total = whitespace + lower + upper + symbols

print(whitespace / total)
print(lower / total)
print(upper / total)
print(symbols / total)