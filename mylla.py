n = int(input())
s = input()
a = 0
h = 0
ac = 0
hc = 0
for ch in s:
    if ch == 'A':
        ac += 1
        if ac == 3:
            a += 1
            ac = 0
            hc = 0
    else:
        hc += 1
        if hc == 3:
            h += 1
            ac = 0
            hc = 0
    if a == n:
        print("Hannes")
        break
    if h == n:
        print("Arnar")
        break