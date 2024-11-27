input()

award_universities = set()
awards = 0
while awards < 12:
    university, team = input().split()
    if university not in award_universities:
        award_universities.add(university)
        print(f"{university} {team}")
        awards += 1
    
