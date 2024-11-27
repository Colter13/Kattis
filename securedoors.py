in_building = set()
for i in range(int(input())):
    action, name = input().split()
    if action == "entry":
        if name in in_building:
            print(f"{name} entered (ANOMALY)")
        else:
            print(f"{name} entered")
            in_building.add(name)
    else:
        if name in in_building:
            print(f"{name} exited")
            in_building.discard(name)
        else:
            print(f"{name} exited (ANOMALY)")
