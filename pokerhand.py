from collections import Counter

cards = input().split()
strength = Counter(card[:1] for card in cards)
print(max(strength.values()))
