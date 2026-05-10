def leapyear(year):
  if year%4==0:
    if year%100==0:
      if year%400==0:
        return True
      else:
        False
    else:
      True
  else:
    False

def days(month,year):
  days=[31,28,31,30,31,30,31,31,30,31,30,31]
  if month == 2 and leapyear(year):
    return 29
  else:
    x=days[month-1]
    return x

month=int(input("Enter the Month: "))
year=int(input("Enter the Year: "))
z=days(month,year)
print(z)
