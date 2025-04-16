class Student:
  def __init__(self, name, jamb_score, course, admitted=False):
    self.name = name
    self.jamb_score = jamb_score
    self.course = course
    self.admitted = admitted

  # Getters
  def get_name(self):
    return self.name
  
  def get_jamb_score(self):
    return self.jamb_score
  
  def get_course(self):
    return self.course
  
  def get_admitted(self):
    return self.admitted
  
  # Setters
  def set_name(self, name):
    self.name = name
  
  def set_jamb_score(self, jamb_score):
    self.jamb_score = jamb_score
  
  def set_course(self, course):
    self.course = course
  
  def set_admitted(self, admitted):
    self.admitted = admitted