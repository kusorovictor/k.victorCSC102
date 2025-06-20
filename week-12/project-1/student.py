class Student:
  def __init__(self, matric: int, name: str, age: int, grade: int):
    self.__matric = matric
    self.__name = name
    self.__age = age
    self.__grade = grade
  
  # Getters
  def get_matric(self) -> int:
    return self.__matric
  
  def get_name(self) -> str:
    return self.__name
  
  def get_age(self) -> int:
    return self.__age
  
  def get_grade(self) -> int:
    return self.__grade
  
  # Setters
  def set_matric(self, matric: int) -> None:
    self.__matric = matric
  
  def set_name(self, name: str) -> None:
    self.__name = name
  
  def set_age(self, age: int) -> None:
    self.__age = age
  
  def set_grade(self, grade: int) -> None:
    self.__grade = grade
  
  
  def to_string(self) -> str:
    return f"Matric: {self.__matric}, Name: {self.__name}, Age: {self.__age}, Grade: {self.__grade}"  