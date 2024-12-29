l = 0
while True:
    l += 1
    n = int(input())
    if n == 0:
        break
    animals = {}
    types = []
    for i in range(n):
        name = list(input().split())
        animal = name[-1].lower()
        if animal in animals:
            animals[animal] += 1
        else:
            animals[animal] = 1
            types.append(animal)
    
    print(f"List {l}:")
    for t in sorted(types):
        print(f"{t} | {animals[t]}")