for i in range(int(input())):
    length, words = map(int, input().split())
    word_list = [input() for i in range(words)]
    characters = length
    for i in range(words-1):
        max_overlap = 0
        for overlap in range(length, 0, -1):
            if word_list[i].endswith(word_list[i+1][:overlap]):
                max_overlap = overlap
                break
        characters += length - max_overlap
    print(characters)
