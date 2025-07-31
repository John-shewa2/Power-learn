# University grading program 
# If grade is 90 or higher, print "A"
#Else if grade is 80 or higher, print "B"
#Else if grade is 70 or higher, print "C"
#Else if grade is 60 or higher, print "D"
#Else, print "F"

score = int(input("What is the score of the student: "))

if score >= 90:
    print("Grade is A: Excellent")
elif score >= 80:
    print("Grade is B: Very Good")
elif score >= 70:
    print("Grade is C: Good")
elif score >= 60:
    print("Grade is d: Satisfactory")
else:
    print("Grade is F: Failed")