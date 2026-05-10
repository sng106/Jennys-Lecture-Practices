student_data=[
{'name':"Ram",
 "roll_no":10,
 "age":20,
 "course":"Python"},
  
{'name':'Mohan',
 "roll_no":20,
 "age":22,
 "course":"Java"}]

def add_new_student(name,rollno,age,course):
  new_student={}
  new_student["name"]=name
  new_student["roll_no"]=rollno
  new_student["age"]=age
  new_student["course"]=course
  student_data.append(new_student)

add_new_student("Shyam",180072, 23, 'Python')

for i in student_data:
  print(i)
  print()
