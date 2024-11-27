sentences = int(input())
for i in range(sentences):
    sentence = input()
    print(sentence[0].upper() + sentence[1:].lower())
