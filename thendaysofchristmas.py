n = int(input())
gifts = [1]
for i in range(2, n+1):
    gifts.append(gifts[-1]+i)
print(gifts[-1], sum(gifts), sep='\n')