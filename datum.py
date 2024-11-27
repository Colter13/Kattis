key_values = {1: 11, 2: 14, 3: 14, 4: 10,
              5: 12, 6: 15, 7: 10, 8: 13,
              9: 16, 10: 11, 11: 14, 12: 16}
days_of_the_week = ["Saturday", "Sunday", "Monday", "Tuesday",
                    "Wednesday", "Thursday", "Friday"]
day, month = map(int, input().split())
print(days_of_the_week[(key_values[month] + day) % 7])
