def check_grades(course):
  
  if(course == "Computer Science"):
    subjects = ["Math", "English", "Biology", "Physics", "Chemistry"]
  elif(course =="Mass Communication"):
    subjects = ["Math", "English", "Literature", "History", "French"]
  passing_grades = 0
  
  for subject in subjects:
    while True:
      grade = input(f"Enter your letter grade for {subject} (A/B/C/D/E/F): ").upper()
      if grade in ['A', 'B', 'C', 'D','E', 'F']:
        print(f"{subject}: {grade}")
        if grade in ['A', 'B', 'C']:
          passing_grades += 1
        break
      else:
        print("Please enter a valid grade (A/B/C/D/E/F)")
  
  print(f"\nNumber of subjects with grade C or better: {passing_grades}\n")
  return passing_grades == 5

