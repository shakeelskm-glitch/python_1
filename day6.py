'''
#bubble sort
numbers=[1,70,45,67,45]
n=len(numbers)
for i in range(n):
    for j in range(0,n-i-1):
        if numbers[j]>numbers[i]:
            numbers[j],numbers[j+1]=numbers[j+1],numbers[j]
print(numbers)''

#selection sort
num=list(map(int,input().split()))
n=len(num)
for i in range(n):
    min_index=i
    for j in range(i+1,n):
        if num[j]<num[min_index]:
            min_index=j
    num[i],num[min_index]=num[min_index],num[i]
print(num)''

#insertion sort
num=list(map(int,input().split()))
n=len(num)
for i in range(1,n):
    key=num[i]
    j=i-1
    while j>=0 and num[j]>key:
        num[j+1]=num[j]
        j-=1
    num[j+1]=key
print(num)
''
def part(arr,low,high):
    pivot=arr[high]
    i=low-1

    for j in range(low,high):
        if arr[j]<=pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1
def quick(arr,low,high):
    if low<high:
        pivot_index=part(arr,low,high)
        quick(arr,low,pivot_index-1)
        quick(arr,pivot_index+1,high)
numbers=list(map(int,input("enter elements:").split()))
quick(numbers,0,len(numbers)-1)
print(numbers)

''


x=[1,2,3]
if x:
    print("not empty")

score = 85 
if score >= 90: 
    print("A") 
elif score >= 80: 
    print("B") 
elif score >= 70: 
    print("C")

for i in range(2,10,3):
    print(i, end=" ")''
    
    
x = 3

while x > 0:
    x -= 1

print(x)''
def add(a, b=5):
    return a + b

print(add(3))''
n = int(input())
r= 0
while n != 0:
    digit = n % 10
    r = r * 10 + digit
    n = n //10

print("Reversed number:", r)''

for i in range(1,50):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0 :
        print("Buzz")
    else:
       print(i)''
num=int(input("Enter a number: "))
factorial=1
for i in range(1, num+1):
    factorial *= i
print("Factorial of", num, "is:", factorial)''
s=input()
v=0
c=0
for ch in s:
    if ch.isalpha():
        if ch in "aeiouAEIOU":
            v+= 1
        else:
            c+= 1
print({"Vowels":v, "Consonants":c})''
start=int(input())
end=int(input())
total=0
for i in range ( start, end+1):
    if i%2==0:
        total+=i
print(total)
''
for num in range(2,101):
    is_prime=True
    for i in range(2,num):
        if num%i==0:
            is_prime=False
            break

print(num)''
def is_prime(n):
    if n <= 1:
        return False 
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
num=int(input())
print(is_prime(num))''
words = input().split()
p = []
n = []
for i in words:
    if i == i[::-1]:
        p.append(i)
    else:
        n.append(i)
print("Palindrome:", p)
print("Non-palindrome:", n)''
t = tuple(map(int, input().split()))
m = t[0]
p = []
o = []

for i in t:
    if i > m:
        m = i
    if i % 2 != 0:
        o.append(i)
    if i > 1:
        f = 0
        for j in range(2, i):
            if i % j == 0:
                f = 1
                break
        if f == 0:
            p.append(i)

print("Maximum:", m)
print("Prime:", p)
print("Odd:", o)''
def fib(n):
    a, b = 0, 1
    l = []
    for i in range(n):
        l.append(a)
        a, b = b, a + b
    return l

def dup(l):
    u = []
    d = []
    for i in l:
        if i not in u:
            u.append(i)
        elif i not in d:
            d.append(i)
    return u, d

lst = fib(int(input("Enter n: ")))
lst += [1, 2, 3, 5]   # adding duplicates

u, d = dup(lst)

print("Without duplicates:", u)
print("Duplicate values:", d)'''
s = input().lower()
w = s.split()
f = {}
v = []
c = []

for i in w:
    f[i] = f.get(i, 0) + 1

for i in s:
    if i.isalpha():
        if i in "aeiou":
            v.append(i)
        else:
            c.append(i)

print("Word Frequency:", f)
print("Vowels:", v)
print("Consonants:", c)
print("Vowel Count:", len(v))
print("Consonant Count:", len(c))