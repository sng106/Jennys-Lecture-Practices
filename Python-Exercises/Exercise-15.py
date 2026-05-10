#Showing grades of studets marks using Dictionary
student_marks={
  'Jenny':92,
  'Harry':78,
  'Dimpy':56,
  'Rahul':41,
  'Ankit':99,
  'Prem':34,
}
student_grades={}
for i in student_marks:
  marks=student_marks[i]
  if marks>90:
    student_grades[i]= 'A+'
  elif marks>80:
    student_grades[i] = "A"
  elif marks > 70:
    student_grades[i] = "B+"
  elif marks > 60:
    student_grades[i] ="B"
  elif marks > 50:
    student_grades[i]= "C"
  elif marks > 40:
    student_grades[i] = "D"
  else:
    student_grades[i]="F"
for j in student_grades.items():
  print(j)
  print()
