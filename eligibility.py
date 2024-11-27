for i in range(int(input())):
    # Initialize input
    student_name, education_start, date_of_birth, courses_completed = input().split()
    education_start_year = int(education_start[:4])
    birth_year = int(date_of_birth[:4])
    courses_completed = int(courses_completed)

    # Determine eligibility
    if education_start_year >= 2010:
        print(f"{student_name} eligible")
    elif birth_year >= 1991:
        print(f"{student_name} eligible")
    elif courses_completed > 40:
        print(f"{student_name} ineligible")
    else:
        print(f"{student_name} coach petitions")    
