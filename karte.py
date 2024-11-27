data= []
for i in range(int(input())):
    data.append(list(input().split()))
    if data[i][0].isdigit():
        data[i][0], data[i][1] = data[i][1], int(data[i][0]) * 2
    
