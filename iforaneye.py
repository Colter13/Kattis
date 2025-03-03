subs = {'at': '@',
        'At': '@',
        'and': '&',
        'And': '&',
        'one': '1',
        'One': '1',
        'won': '1',
        'Won': '1',
        'to': '2',
        'To': '2',
        'too': '2',
        'Too': '2',
        'two': '2',
        'Two': '2',
        'for': '4',
        'For': '4',
        'four': '4',
        'Four': '4',
        'bea': 'b',
        'Bea': 'B',
        'be': 'b',
        'Be': 'B',
        'bee': 'b',
        'Bee': 'B',
        'sea': 'c',
        'Sea': 'C',
        'see': 'c',
        'See': 'C',
        'eye': 'i',
        'Eye': 'I',
        'oh': 'o',
        'Oh': 'O',
        'owe': 'o',
        'Owe': 'O',
        'are': 'r',
        'Are': 'R',
        'you': 'u',
        'You': 'U',
        'why': 'y',
        'Why': 'Y'}

for _ in range(int(input())):
    words = list(input().split(" "))
    abridged = []

    for word in words:
        if len(word) == 1:
            abridged.append(word)
        elif len(word) == 2:
            if word in subs:
                abridged.append(subs[word])
            else:
                abridged.append(word)
        else:
            start = 0
            new_word = ""
            while start < len(word):
                if start + 3 < len(word) and word[start:start+4] in subs:
                    new_word += subs[word[start:start+4]]
                    start += 4
                elif start + 2 < len(word) and word[start:start+3] in subs:
                    new_word += subs[word[start:start+3]]
                    start += 3
                elif start + 1 < len(word) and word[start:start+2] in subs:
                    new_word += subs[word[start:start+2]]
                    start += 2
                else:
                    new_word += word[start]
                    start += 1
            abridged.append(new_word)
    print(*abridged)