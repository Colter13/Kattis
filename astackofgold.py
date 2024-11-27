weight, stacks = map(int, input().split())
tungsten = 29260
gold = 29370
expected = sum([tungsten * i for i in range(stacks+1)])
print((weight-expected)//(gold-tungsten))