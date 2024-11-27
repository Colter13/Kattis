runners = []

# input
for i in range(int(input())):
    name, start, relay = input().split()
    start = float(start)
    relay = float(relay)
    runners.append((name, start, relay))

runners = sorted(runners, key=lambda x: x[2])
gimmes = runners[:3]
remaining = runners[3:]
re_remaining = remaining[0]
st_remaining = sorted(remaining, key=lambda x: x[1])[0]
gimmes = sorted(gimmes, key=lambda x: x[1]-x[2])

if gimmes[0][1]+re_remaining[2] < gimmes[0][2]+st_remaining[1]:
    print(gimmes[0][1]+re_remaining[2]+gimmes[1][2]+gimmes[2][2])
    print(gimmes[0][0], gimmes[1][0], gimmes[2][0], re_remaining[0], sep='\n')
else:
    print(gimmes[0][2]+st_remaining[1]+gimmes[1][2]+gimmes[2][2])
    print(st_remaining[0], gimmes[0][0], gimmes[1][0], gimmes[2][0], sep='\n')