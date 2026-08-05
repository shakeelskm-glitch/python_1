#bank balance
balance=1000
print("Initial balance:", balance)
withdraw=int(input("Enter amount to withdraw: "))
deposit=int(input("Enter amount to deposit: "))
if withdraw<=balance:
    balance-=withdraw
    print("Balance after withdrawal:", balance)
elif deposit>0:
    balance+=deposit
    print("Balance after deposit:", balance)
else:
    print("Invalid transaction. Please check your input.")


#employee id
e1=int(input("Enter employee id: "))
e2=int(input("Enter employee id: "))    
if e1>e2:
    print("Employee 1 has a higher id") 
elif e1<e2:
    print("Employee 2 has a higher id")
else:
    print("Both employees have the same id")

#login authentication system
username=input("Enter username: ")
password=input("Enter password: ")
if username=="admin" and password=="password":
    print("Login successful.")
else:
    print("Invalid username or password.")