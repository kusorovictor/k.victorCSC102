import check
import interview

def comp_sci(jamb_score):
    if jamb_score >= 250:
        check.check_grades("Computer Science")
        interview.interview_stuff()
    else:
        print("You do not meet the JAMB score requirement for Computer Science.")
        return False
    
    
def mass_comm():
    check.check_grades("Mass Communication")    
    interview.interview_stuff()