alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

message, key = input(), input()

decoded = ''
decoded_ch = ''

for i in range(len(message)):
    decoded_ch = alphabet[(alphabet.index(message[i]) - alphabet.index(key[i]) % 26)]
    key += decoded_ch
    decoded += decoded_ch
print(decoded)
