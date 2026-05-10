#Printing average height without using len and sum function
#my code
hh = [151, 153, 160, 140]
total = 0
for i in hh:
    total=total+i
  
avg=total/4
print(round(avg))
'''---------------------------------------------------'''
# jenny code with proper tricks
height=input("Enter your height in cm: ")
heightaslist=height.split()
print(heightaslist)
print("type: ", type(heightaslist[0]))
#Getting length of input without using len function
count=0
for heigh in heightaslist:
  count+=1
print(count)
#Converting the list of strings to list of integers
for i in range(count):
  heightaslist[i]=int(heightaslist[i])
print(heightaslist)
print("type: ", type(heightaslist[0]))
#Calculating the average height
sum=0
for average in heightaslist:
 sum+=average
print(sum)
print()
print(f"The average height is {round(sum/count)}")
