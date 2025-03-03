class node:
    def __init__(self, value, parent, numChildren):
        self.value = value
        self.parent = parent
        self.numChildren = numChildren
    def addChild():
        self.numChildren += 1

n, k = map(int, input().split())
x = list(map(int, input().split()))
parents = {1:0}
weight = {1:1}
for i in range(n-1):
    weight[i+2] = 0
    parents[i+2] = x[i]
    parent = x[i]
    while parent != 0:
        weight[parent] += 1
        parent = parents[parent]
print(weight)

print(parents)
    
    