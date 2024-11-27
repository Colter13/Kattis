vowels = ['a','e','i','o','u']

sentence = list(input())

decoded = ''

i = 0
while True:
    if i >= len(sentence):
        break
    if sentence[i] in vowels:
        decoded += sentence[i]
        i += 2
    else:
        decoded += sentence[i]
    i += 1

print(decoded)