#Choosing of a guy who pay the bill in a friends gang

import random

names=input("Enter the names: ").split(",")
print(names)
rant=random.randint(0,len(names)-1)
print(names[rant])

