#Showing, depositing and withdrawling details of Bank Account using Class and Objects

class BankAccount:
	def __init__(self,name,balance=0):
		self.name=name
		self.balance=balance
		
	def deposit(self,amount):
		self.balance=self.balance+amount #amount is a parameter so no need of self.amount
		print("Cash Deposited")
		
	def withdraw(self,amount):
		if amount > self.balance:
			print("Not Enough Balance")
		else:
			self.balance=self.balance-amount
			print("Cash Withdrawed")
			
	def __str__(self):
		return f"Account Holder Name: {self.name}\nBalance: {self.balance}"

s1=BankAccount("Mohan", 49000)
msg='''
1. Balance Check 
2. Deposit
3. Withdraw 
4. Exit
'''
print(msg)
z=False
while not z:
	ch=input("Enter Your Choice: ")
	if ch == '1':
		print(s1)
	elif ch == '2':
		amount=int(input("How much you need to deposit: "))
		s1.deposit(amount)
		print(s1)
	elif ch == '3':
		amount=int(input("How much you need to withdraw: "))
		s1.withdraw(amount)
		print(s1)
	elif ch == '4':
		print("Thank You")
		z=True
	else:
		print("Input is wrong, Kindly use proper Input")
		z=True
	
