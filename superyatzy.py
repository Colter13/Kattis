n, m = map(int, input().split())
dice_count = dict()
for i in range(n):
    dice = int(input())
    if dice in dice_count:
        dice_count[dice] += 1
    else:
        dice_count[dice] = 1

print("Ja" if (n - max(dice_count.values())) <= m else "Nej" )