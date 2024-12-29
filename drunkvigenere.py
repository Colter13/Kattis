letters = "abcdefghijklmnopqrstuvwxyz".upper()

encoded = input()
key = input()

decoded = ''

for i, ch in enumerate(encoded):
    shift = letters.index(key[i])
    if i % 2 != 0:
        decoded += letters[(letters.index(encoded[i])+shift) % 26]
    else:
        decoded += letters[(letters.index(encoded[i])-shift) % 26]

print(decoded)