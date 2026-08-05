#reverse numbers from 1 to n
num=int(input("Enter a number: "))
for i in range(num, 0, -1):
    print(i, end=" \n")

#count characters in a string
name=input("Enter a string: ")
print(len(name))

#calculator
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)
print("Quotient:", a / b)

#calculator
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
operation=input("Enter operation ")
if operation=="+":
    print("sum=",a+b)
elif operation=="-":
    print("difference=",a-b)
elif operation=="*":
    print("product=",a*b)
elif b!=0 and operation=="/":
    print("quotient=",a/b)
else:
    print("invalid operation or division by zero")


#count characters in a string
name=input("Enter a string: ")
if name.isalpha():
    print("Number of characters in the string:", len(name))
else:
    print("Invalid input. Please enter a string containing only alphabetic characters.")\

#leap year
year=int(input("Enter a year: "))
if year%4==0:
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")

#vowels in a string
name=input("Enter a string: ")
vowels="aeiouAEIOU"
count=0
for char in name:
    if char in vowels:
        count+=1
print("Number of vowels in the string:", count)

#swap two numbers using if
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    temp = a
    a = b
    b = temp
print("After swapping: a=", a, "b=", b)
