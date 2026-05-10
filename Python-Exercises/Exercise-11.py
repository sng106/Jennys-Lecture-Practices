#sum of even numbers between 1 to 100 including 1,100

sum=0
for i in range(1,101):
  if i%2==0:
    print(i)
    sum+=i
print(sum)
