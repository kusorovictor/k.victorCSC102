import random
import time

def interview_result():
  chance = random.randint(1, 100)

  if chance <= 30:
    return True
  else:
    return False

def interview_stuff():
  print("We are preparing an interview for you. Please wait....")
  print("Your interview is in progress..... ")
  time.sleep(5)
  
  if(interview_result == False):
      print("You have failed your interview and will not be admitted.")
      return False
  else:
      print("Congratulations! You have passed the interview and will be admitted.")
      print("You will be contacted via email with further instructions.")
      print("Thank you for your patience.")
      return True