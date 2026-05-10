#Finding the maximum value without using max function

numbers=input("Enter the numbers: ")
print()
print("Value as string: ",numbers)
print()
numberaslist=numbers.split()
print("Value as list: ",numberaslist)
print()
count=0
for he in numberaslist:
  count=count + 1
print("Count is: ",count)
print()
#list into integers
for inn in range(count):
  numberaslist[inn]=int(numberaslist[inn])
print("Value as integer: ",numberaslist)

max_val=numberaslist[0]
for i in numberaslist:
  if i > max_val:
    max_val=i
print()
print("The Maximum Value is: ",max_val)
