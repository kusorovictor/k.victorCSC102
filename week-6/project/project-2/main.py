import course as cs

name = input("Enter your full name: ")

jamb_score = int(input("Enter your JAMB score: "))
if jamb_score < 230:
    print("You do not meet the JAMB score requirement for any of the courses available.")
else:
    course = input("Enter your preferred course (Computer Science/Mass Communication): ").strip().lower()
    if course == "computer science":
        cs.comp_sci(jamb_score)
    elif course == "mass communication":
        cs.mass_comm()
    else:
        print("Invalid course selection. Please choose either 'Computer Science' or 'Mass Communication'.")