#time=float(input())
#if time<=9:
#    print("get in to class")
#else:
#    print("not allowed to enter class")

num=[10,12,13,14,16]
print(num[1:])

#prime
for num in range(2,101):
    is_prime=True
    for i in range(2,num):
        if num%i==0:
            is_prime=False
            break
    if is_prime:
        print(num)

#fibonacci series
n=int(input("Enter the number of terms: "))
a=0
b=1
for _ in range(n):
    print(a, end=" ")
    a,b=b,a+b


#sum of n natural numbers
n=int(input("Enter a number: "))
sum=0
for i in range(1,n+1):
    sum+=i
print("Sum of first", n, "natural numbers is:", sum)

#armstrong number
num=int(input("Enter a number: "))
temp=num
sum=0
while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=10
if num==sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")

#palindrome number
num=int(input("Enter a number: "))
rev_str=str(num)[::-1]
rev=int(rev_str)
num=int(num)
if num==rev:
    print(num, "is a palindrome number")    
else:
    print(num, "is not a palindrome number")

#factorial
num=int(input("Enter a number: "))
factorial=1
for i in range(1, num+1):
    factorial *= i
print("Factorial of", num, "is:", factorial)

#star pattern
n=int(input("Enter the number of rows: "))
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()