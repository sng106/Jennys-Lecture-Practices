'''Pizza Order:
Condions: 
Small Pizza = 100
Medium Pizza = 200
Lerge Pizza = 300
Pepperoni for small Pizza = 30
Pepperoni for medium or Large Pizze = 50
Extra cheese for any Pizza = 20
'''

pizza = input("Which Size of Pizza want S/M/L: ")
print()
bill = 0
if pizza == "s" or pizza == "S":
  bill = bill + 100
  print("The Rate of Small pizza is 100")
  print()
elif pizza == "m" or pizza == "M":
  bill = bill + 200
  print("The Rate of Medium pizza is 200")
  print()
elif pizza == "l" or pizza == "L":
  bill = bill + 300
  print("The Rate of Large pizza is 300")
  print()
pepper= input("Need Pepper: ")
print()
if pepper == "y" or pepper == "Y":
  if pizza == "s" or pizza == "S":
    bill+=30
  else:
    bill+=50
cheese = input("Need Cheese: ")
if cheese == "y" or cheese == "Y":
  bill+=20
print()
print("The Total Bill is: ",bill)
