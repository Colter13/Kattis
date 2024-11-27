lower_limit, upper_limit = map(int, input().split())

combinations = 0
for i in range(lower_limit, upper_limit + 1):
    i_str = str(i)
    for j in range(6):
        if i_str[j] == '0' or i % int(i_str[j]) != 0 or len(set(i_str)) != len(str(i)):
            break
        if j == 5:
            combinations += 1
print(combinations)
