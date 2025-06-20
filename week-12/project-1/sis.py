import student
import pandas as pd
 
class Sis: 
    def __init__(self):
      try:
          self.df = pd.read_csv(r'C:/Users/eastw/Git Projects/School/k.victorCSC102/week-12/project-1/SIS.csv')
          print(f"Successfully read CSV with {len(self.df)} rows")
      except FileNotFoundError:
          print("Error: CSV file not found at specified path")
          raise
      except pd.errors.EmptyDataError:
          print("Error: CSV file is empty")
          raise
      except Exception as e:
          print(f"Error reading CSV: {str(e)}")
          raise
          
      self.__students = []
      self.populate_students()


    # Populate the students list with Student objects from the DataFrame
    def populate_students(self):
        for index, row in self.df.iterrows():
          matric = row['MatNo']
          name = row['Name']
          age = row['Age']
          grade = row['Grade']
          student_obj = student.Student(matric, name, age, grade)     
          print(f"Adding student: {student_obj.to_string()}")
          
          # Check if student with same matric number already exists
          if not any(s.get_matric() == student_obj.get_matric() for s in self.__students):
              self.__students.append(student_obj)
          else:
              print(f"Warning: Student with matric {student_obj.get_matric()} already exists")
          
    def get_students(self):
        return self.__students    
