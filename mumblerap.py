n = int(input())
string = input()
cur_largest = 0
temp = ""
for i in range(n):
    if string[i].isdigit():
        temp += string[i]
    elif temp == "":
        pass
    else:
        if int(temp) > cur_largest:
            cur_largest = int(temp)
        temp = ""
if temp != "" and int(temp) > cur_largest:
    cur_largest = int(temp)
print(cur_largest)
