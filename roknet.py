values = {}
for i in range(int(input())):
    x = list(input().split())
    if x[0] == "INNTAK":
        values[x[1]] = (x[2] == "SATT")
    elif x[0] == "EKKI":
        values[x[2]] = not values[x[1]]
    elif x[0] == "OG":
        values[x[3]] = values[x[1]] and values[x[2]]
    elif x[0] == "EDA":
        values[x[3]] = values[x[1]] or values[x[2]]
    else:
        print(x[1], "SATT" if values[x[1]] == 1 else "OSATT")