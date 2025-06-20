import sis
import pandas as pd

students = sis.Sis().get_students()

def get_student_in_age_range(min_age: int, max_age: int):
    return [student for student in students if min_age < student.get_age() < max_age]

def create_csv_and_map_students(filename: str, students_list):
    df = pd.DataFrame({
        'Matric_No': [student.get_matric() for student in students_list],
        'Name': [student.get_name() for student in students_list],
        'Age': [student.get_age() for student in students_list],
        'Grade': [student.get_grade() for student in students_list]
    })
    
    for student in students_list:
        print(f"Matric: {student.get_matric()}, Name: {student.get_name()}, Age: {student.get_age()}, Grade: {student.get_grade()}")
    print()
    
    #Create the csv file
    df.to_csv(filename, index=False)


def run_app():
    #The Pirates
    print("\nThe Pirates")
    the_pirates = get_student_in_age_range(14, 18)
    create_csv_and_map_students('The_Pirates.csv', the_pirates)
    
    #The Yankees
    print("The Yankees")
    the_yankees = get_student_in_age_range(18, 22)
    create_csv_and_map_students('The_Yankees.csv', the_yankees)

    #The Bulls
    print("The Bulls")
    the_bulls = get_student_in_age_range(22, 25)
    create_csv_and_map_students('The_Bulls.csv', the_bulls)
    
    #Check if the student is over 25
    print("Is over 25?")
    over_age = [student for student in students if student.get_age() >= 25]
    if over_age:
      print("Error: The following students are over the age limit of 25:")
      for student in over_age:
        print(f"Name: {student.get_name()}, Age: {student.get_age()}")


def __main__():
  run_app()
    
if __name__ == "__main__":
   __main__()