import course as cs
import student as S;
admitted_students = []
non_admitted_students = []

while True:
    name = input("Enter your full name (or 'q' to quit): ")
    if name.lower() == 'q':
        break
        
    jamb_score = int(input("Enter your JAMB score: "))
        
    if jamb_score < 230:
            print("You do not meet the JAMB score requirement for any of the courses available.")
            student = S.Student(name, jamb_score, "None", False)
            non_admitted_students.append(student)
            
    else:
        course = input("Enter your preferred course (Computer Science/Mass Communication): ").strip().lower()
        if course == "computer science":
            admitted = cs.comp_sci(jamb_score)
            print("Admitted: ", admitted)
            student = S.Student(name, jamb_score, "Computer Science", admitted)
            admitted_students.append(student)
            
        elif course == "mass communication":
            admitted = cs.mass_comm()
            student = S.Student(name, jamb_score, "Computer Science", admitted)
            admitted_students.append(student)
            
        else:
            print("Invalid course selection. Please choose either 'Computer Science' or 'Mass Communication'.")
            continue
    
        

def print_student_tables():
    print("\nADMITTED STUDENTS")
    print("-" * 60)
    print(f"{'Name':<30} {'JAMB Score':<15} {'Course':<20}")
    print("-" * 60)
    for student in admitted_students:
        print(f"{student.get_name():<30} {student.get_jamb_score():<15} {student.get_course():<20}")

    print("\nNON-ADMITTED STUDENTS")
    print("-" * 60)
    print(f"{'Name':<30} {'JAMB Score':<15} {'Course':<20}")
    print("-" * 60)
    for student in non_admitted_students:
        print(f"{student.get_name():<30} {student.get_jamb_score():<15} {student.get_course():<20}")

print_student_tables()
print(f"\nTotal Admitted Students: {len(admitted_students)}")
print(f"Total Non-Admitted Students: {len(non_admitted_students)}")
