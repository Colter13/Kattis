n = int(input())
names = []
prefix = []
while n != 0:
    for i in range(n):
        sort_name = input()
        matching = False
        matching_index = -1
        for i in range(len(names)):
            if sort_name[:2] == names[i][:2]:
                matching = True
                matching_index = i
        if matching:
            names.insert(matching_index, sort_name)
        else:
            fake_names = names
            fake_names.append(sort_name)
            names.insert(sorted(fake_names).index(sort_name), sort_name)
            print(names, fake_names)
            fake_names = []
            
            
    print('\n'.join(sorted(names)))
    n = int(input())
    if n == 0:
        break
    else:
        print()
        names.clear()
