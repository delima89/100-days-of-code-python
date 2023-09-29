student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades={}

#TODO-2: Write your code below to add the grades to student_grades.👇
for notas in student_scores:
    print(notas)
    print(student_scores[notas])
    if student_scores[notas] >= 90 and student_scores[notas] <= 100:
        student_grades[notas]= "Outstanding"
    elif student_scores[notas] >= 81 and student_scores[notas] <= 90:
        student_grades[notas]= "Exceeds Expectations"
    elif student_scores[notas] >= 71 and student_scores[notas] <=80:
        student_grades[notas]= "Acceptable"
    else:
        student_grades[notas]= "Fail"

print(student_grades)