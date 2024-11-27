views = {}
for i in range(int(input())):
    name, view_count = input().split()
    view_count = int(view_count)
    if name in views:
        views[name] += view_count
    else:
        views[name] = view_count
cur_name = ""
cur_value = 0
for key, value in views.items():
    if value > cur_value:
        cur_name = key
        cur_value = value
print(cur_name)