'''
LOVE CALCULATOR:
TRUELOVE: Check how many truelove letters in Name of he and she
eg: He has 5 and She has 2 output should be 52 '''

name1=input("Enter his name: ")
name2=input("Enter her name: ")
combine=name1+name2
lower=combine.lower()
t=lower.count("t")
r=lower.count('r')
u=lower.count('u')
e=lower.count('e')
l=lower.count("l")
o=lower.count("o")
v=lower.count("v")
e=lower.count("e")
true=t+r+u+e
love=l+o+v+e
print(f"Your love score is {true}{love}%")
