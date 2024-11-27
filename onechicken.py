chicken, people = map(int, input().split())
difference = people - chicken
if difference == 1:
    print("Dr. Chaz will have 1 piece of chicken left over!")
elif difference == -1:
    print("Dr. Chaz needs", 1, "more piece of chicken!")
elif difference > 0:
    print("Dr. Chaz will have", difference, "pieces of chicken left over!")
else:
    print("Dr. Chaz needs", abs(difference), "more pieces of chicken!")
