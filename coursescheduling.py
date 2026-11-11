from collections import defaultdict

requests = []

for i in range(int(input())):
    fn, ln, course = input().split()
    name = fn + ln
    requests.append([name, course])
    
courses = {}
out = []
prev = ""
prev_course = ""
for i in range(len(requests)):
    if requests[i][0] == prev and requests[i][1] == prev_course:
        continue
    if requests[i][1] in courses:
        courses[requests[i][1]] += 1
    else:
        out.append(requests[i][1])
        courses[requests[i][1]] = 1
    prev = requests[i][0]
    prev_course = requests[i][1]
for course in sorted(out):
    print(course, courses[course])
    