'''#program to reverse a queue without using built-in reverse() functions
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Dequeue from empty queue")

    def size(self):
        return len(self.items)

    def reverse(self):
        if self.is_empty():
            return
        item = self.dequeue()
        self.reverse()
        self.enqueue(item)

    def display(self):
        print("Queue:", self.items)''

#or

queue=[]
n=int(input("Enter the number of elements in the queue: "))
for i in range(n):
    element=int(input("Enter element: "))
    queue.append(element)
print("Original Queue:", queue)
stack=[]
while len(queue) > 0:
    stack.append(queue.pop(0))
while len(stack) > 0:
    queue.append(stack.pop())
print("Reversed Queue:", queue)
''
#program to seperate the elements of a queue into even and odd queues
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Dequeue from empty queue")

    def size(self):
        return len(self.items)

    def display(self):
        print("Queue:", self.items)

    def separate_even_odd(self):
        even_queue = Queue()
        odd_queue = Queue()
        while not self.is_empty():
            item = self.dequeue()
            if item % 2 == 0:
                even_queue.enqueue(item)
            else:
                odd_queue.enqueue(item)
        return even_queue, odd_queue

    def display_separated(self):
        even_queue, odd_queue = self.separate_even_odd()
        print("Even Queue:", even_queue.items)
        print("Odd Queue:", odd_queue.items)
q=Queue()
n=int(input("Enter the number of elements in the queue: "))
for i in range(n):
    element=int(input("Enter element: "))
    q.enqueue(element)
q.display_separated()
''

#program to merge two queues into a single queue while preserving the order of elements
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Dequeue from empty queue")

    def size(self):
        return len(self.items)

    def display(self):
        print("Queue:", self.items)

    @staticmethod
    def merge_queues(queue1, queue2):
        merged_queue = Queue()
        while not queue1.is_empty() or not queue2.is_empty():
            if not queue1.is_empty():
                merged_queue.enqueue(queue1.dequeue())
            if not queue2.is_empty():
                merged_queue.enqueue(queue2.dequeue())
        return merged_queue

    def display_merged(self, queue1, queue2):
        merged_queue = self.merge_queues(queue1, queue2)
        print("Merged Queue:", merged_queue.items)
q=Queue()
n1=int(input("Enter the number of elements in the first queue: "))
for i in range(n1):
    element=int(input("Enter element for first queue: "))
    q.enqueue(element)
q2=Queue()
n2=int(input("Enter the number of elements in the second queue: "))
for i in range(n2):
    element=int(input("Enter element for second queue: "))
    q2.enqueue(element)

''
#program to compare two queues and check if they contain the same elements in the same order
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Dequeue from empty queue")

    def size(self):
        return len(self.items)

    def display(self):
        print("Queue:", self.items)

    @staticmethod
    def compare_queues(queue1, queue2):
        if queue1.size() != queue2.size():
            return False
        for i in range(queue1.size()):
            if queue1.items[i] != queue2.items[i]:
                return False
        return True

    def display_comparison(self, queue1, queue2):
        if self.compare_queues(queue1, queue2):
            print("The queues are the same.")
        else:
            print("The queues are different.")
q=Queue()
n1=int(input("Enter the number of elements in the first queue: "))
for i in range(n1):
    element=int(input("Enter element for first queue: "))
    q.enqueue(element)

q2=Queue()
n2=int(input("Enter the number of elements in the second queue: "))
for i in range(n2):
    element=int(input("Enter element for second queue: "))
    q2.enqueue(element)
q.display_comparison(q, q2)

''

#program to rotate a queue by k elements
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Dequeue from empty queue")

    def size(self):
        return len(self.items)

    def display(self):
        print("Queue:", self.items)

    def rotate(self, k):
        if k < 0 or k > self.size():
            raise ValueError("Invalid rotation value")
        for _ in range(k):
            item = self.dequeue()
            self.enqueue(item)

    def display_rotated(self, k):
        self.rotate(k)
        print(f"Queue after rotating by {k} elements:", self.items)

q=Queue()
n=int(input("Enter the number of elements in the queue: "))
for i in range(n):
    element=int(input("Enter element: "))
    q.enqueue(element)
q.rotate(int(input("Enter the number of elements to rotate the queue by: ")))
q.display_rotated(int(input("Enter the number of elements to rotate the queue by: ")))  

''

#Write a Python program to implement a Customer Service Queue. The program should support the following operations:
#	Add Customer
#	Serve Customer
#	Display Waiting Customers
#	Display Front Customer
#	Display Total Customers
class CustomerServiceQueue:
    def __init__(self):
        self.queue = Queue()

    def add_customer(self, customer_name):
        self.queue.enqueue(customer_name)
        print(f"Customer '{customer_name}' added to the queue.")

    def serve_customer(self):
        if not self.queue.is_empty():
            served_customer = self.queue.dequeue()
            print(f"Customer '{served_customer}' has been served.")
        else:
            print("No customers in the queue to serve.")

    def display_waiting_customers(self):
        self.queue.display()

    def display_front_customer(self):
        if not self.queue.is_empty():
            front_customer = self.queue.items[0]
            print(f"Front customer in the queue: '{front_customer}'")
        else:
            print("No customers in the queue.")

    def display_total_customers(self):
        total_customers = self.queue.size()
        print(f"Total customers in the queue: {total_customers}")

c=CustomerServiceQueue()
c.add_customer("Alice")
c.add_customer("Bob")   
c.add_customer("Charlie")
c.display_waiting_customers()
c.display_front_customer()  
c.display_total_customers()
c.serve_customer()
''

#python Math Library
import math
num=int(input("Enter a number:"))
print("Square Root:",math.sqrt(num))
print("Factorial:",math.factorial(num))
base=int(input("\nEnter Base:"))
power=int(input("Enter power:"))
print("power:",math.pow(base,power))
''

#random 
import random
print("Random Integer:",random.randint(1,100))
print("Random Number from Range:",random.randrange(10,50))
print("Random Decimal:",random.uniform(1,10))

fruits=["Apple","Banana"]
print("Random Fruit:",random.choice(fruits))
numbers=[1,2,3,4,5]
random.shuffle(numbers)
print("Shuffled List:",numbers)
''

#datetime
from datetime import datetime,date,timedelta
now=datetime.now()
print("Current Date and Time",now)
today=date.today()
print("Todays date:",today)
print("Year:",now.year)
print("Month:",now.month)
print("Day:",now.day)
print("Hour:",now.hour)
print("Minute:",now.minute)
print("Seconds:",now.second)
print("Formatted Date:",now.strftime("%d-%m-%Y"))
print("Formatted Time:",now.strftime("%H:%M:%S"))
future_date=today+timedelta(days=7)
print("Date After & days:",future_date)
past_date=today-timedelta(days=7)
print("Date before & days:",past_date)''

#time
import time
print("Current Time:",time.time())
print("Readable Time:",time.ctime())
current=time.localtime()
print("Year:",current.tm_year)
print("month:",current.tm_mon)
print("day:",current.tm_mday)
print("Formatted Date:",time.strftime("%d-%m-%Y"))
print("Formatted Time:",time.strftime("%H:%M:%S"))
print("Program Paused for 3 Seconds...")
time.sleep(3)
print("Progress Resumed")
start=time.perf_counter()
for i in range(1000000):
    pass
end=time.perf_counter()
print("Execution Time:",end-start,"seconds")
''


# Statistics Library - Practice Questions Solution

import statistics

numbers = [10, 20, 30, 40, 50, 20, 30]

# Question 1: Find the Mean
print("Q1: Mean =", statistics.mean(numbers))

# Question 2: Find the Median
print("Q2: Median =", statistics.median(numbers))

# Question 3: Find the Mode
print("Q3: Mode =", statistics.mode(numbers))

# Question 4: Find All Modes
print("Q4: Multiple Modes =", statistics.multimode(numbers))

# Question 5: Calculate the Variance
print("Q5: Variance =", statistics.variance(numbers))

# Question 6: Calculate the Standard Deviation
print("Q6: Standard Deviation =", statistics.stdev(numbers))

# Question 7: Find Mean, Median and Mode of Student Marks
marks = [85, 90, 78, 92, 88, 90, 95]

print("\nQ7:")
print("Mean =", statistics.mean(marks))
print("Median =", statistics.median(marks))
print("Mode =", statistics.mode(marks))

# Question 8: Compare Mean and Median
print("\nQ8:")

if statistics.mean(numbers) > statistics.median(numbers):
    print("Mean is Greater than Median")
elif statistics.mean(numbers) < statistics.median(numbers):
    print("Mean is Less than Median")
else:
    print("Mean and Median are Equal")

# Question 9: Check Whether Dataset has One Mode or Multiple Modes
modes = statistics.multimode(numbers)

print("\nQ9:")

if len(modes) == 1:
    print("Dataset has One Mode:", modes[0])
else:
    print("Dataset has Multiple Modes:", modes)

# Question 10: Complete Statistical Analysis
print("\nQ10: Complete Statistical Analysis")
print("Mean =", statistics.mean(numbers))
print("Median =", statistics.median(numbers))
print("Mode =", statistics.mode(numbers))
print("Variance =", statistics.variance(numbers))
print("Standard Deviation =", statistics.stdev(numbers))'''

# NumPy - Practice Questions Solution

import numpy as np

# Question 1: Create a one-dimensional NumPy array containing five integers.
array1 = np.array([10, 20, 30, 40, 50])
print("Q1:")
print(array1)

# Question 2: Create a two-dimensional NumPy array of size 3 × 3.
array2 = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
print("\nQ2:")
print(array2)

# Question 3: Create an array using arange() from 1 to 20.
array3 = np.arange(1, 21)
print("\nQ3:")
print(array3)

# Question 4: Create an array of 10 equally spaced values between 0 and 100.
array4 = np.linspace(0, 100, 10)
print("\nQ4:")
print(array4)

# Question 5: Create a 3 × 4 array filled with zeros.
array5 = np.zeros((3, 4))
print("\nQ5:")
print(array5)

# Question 6: Create a 2 × 5 array filled with ones.
array6 = np.ones((2, 5))
print("\nQ6:")
print(array6)

# Question 7: Find the maximum, minimum, and sum of an array.
numbers = np.array([10, 25, 40, 55, 70])

print("\nQ7:")
print("Maximum:", np.max(numbers))
print("Minimum:", np.min(numbers))
print("Sum:", np.sum(numbers))

# Question 8: Calculate the mean, median, and standard deviation of an array.
print("\nQ8:")
print("Mean:", np.mean(numbers))
print("Median:", np.median(numbers))
print("Standard Deviation:", np.std(numbers))

# Question 9: Reshape a one-dimensional array of 12 elements into a 3 × 4 matrix.
array9 = np.arange(1, 13).reshape(3, 4)

print("\nQ9:")
print(array9)

# Question 10: Display the dimensions, shape, size, and data type of a NumPy array.
print("\nQ10:")
print("Dimensions:", array9.ndim)
print("Shape:", array9.shape)
print("Size:", array9.size)
print("Data Type:", array9.dtype)