n = int(input())
pieces = sorted(list(map(int, input().split())))

alice = 0
bob = 0

for i in range(n):
    if i % 2 == 0:
        alice += pieces.pop()
    else:
        bob += pieces.pop()
        
print(alice, bob)