w = input()
length = len(w)
champ = ""
i = 0
while len(champ) < length:
    i += 1
    champ += str(i)
if champ == w:
    print(i)
else:
    print(-1)
