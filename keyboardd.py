
typed = input()+" "
displayed = input()+" "

sticky_keys = set()
removed = 0

for i in range(len(displayed) - 1):
    if typed[i - removed] != displayed[i]:
        sticky_keys.add(displayed[i])
        removed += 1
if len(displayed) > len(typed) + removed:
    sticky_keys.add(displayed[-1])
        
print(''.join(sticky_keys))

# Kyle's Solution
'''
b = 0
good = input()+" "
bad = input()+" "
sticky = set()

for g in good:
    while bad[b] != g:
        sticky.add(bad[b])
        b += 1
    b += 1

print(''.join(sticky))
'''
