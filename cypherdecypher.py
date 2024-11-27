letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
key = {ch: i for i, ch in enumerate(letters)}
reverse_key = dict(enumerate(letters))

multiplier = input()
for _ in range(int(input())):
    encrypted = ''
    plaintext = input()
    for i in range(len(multiplier)):
        encrypted += reverse_key[(key[plaintext[i]] * int(multiplier[i])) % 26]
    print(encrypted)