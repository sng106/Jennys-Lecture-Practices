def primechecker(number):
  prime=True
  for i in range(2,number):
    if number%i==0:
      prime=False
  if prime is True:
    print("PrimeNUmber")
  else:
    print("Not Prime")
    
number=int(input("Enter the Number You Need to Check: "))
primechecker(number)
