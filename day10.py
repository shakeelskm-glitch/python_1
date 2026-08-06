#stack implementation using list
'''class stack:
    def __init__(self):
        self.stack=[]
    def push(self,item):
        self.stack.append(item)
        print("Item pushed:",item)
    def pop(self):
        if len(self.stack)==0:
            print("stack underflow")
        else:
            print("Item popped:",self.stack.pop())
    def peek(self):
        if len(self.stack)==0:
            print("stack is empty")
        else:
            print("Top item:",self.stack[-1])
    def display(self):
        if len(self.stack)==0:
            print("stack is empty")
        else:
            print("Stack elements:",self.stack)

def stack_operations():
    s=stack()
    while True:
        print("\nStack Operations:")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Display")
        print("5. Exit")
        choice=int(input("Enter your choice: "))
        if choice==1:
            item=int(input("Enter item to push: "))
            s.push(item)
        elif choice==2:
            s.pop()
        elif choice==3:
            s.peek()
        elif choice==4:
            s.display()
        elif choice==5:
            break
        else:
            print("Invalid choice")

stack_operations()
s.display()''


#program to search for given element in stack without modifying it
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) == 0:
            print("Stack underflow")
            return None
        else:
            return self.stack.pop()

    def peek(self):
        if len(self.stack) == 0:
            print("Stack is empty")
            return None
        else:
            return self.stack[-1]

    def display(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        else:
            print("Stack elements:", self.stack)

    def search(self, item):
        if item in self.stack:
            print(f"Item {item} found in stack.")
        else:
            print(f"Item {item} not found in stack.")
s=Stack()
s.push(10)
s.push(20)
s.push(30)
s.search(20)
s.display()

''
#program to reverse a stack
class stack:
    def __init__(self):
        self.stack=[]

    def push(self,item):
        self.stack.append(item)
        print(item,"is pushed")

    def pop(self):
        if len(self.stack)==0:
            print("stack is empty") 
        else:
            print("poped element is",self.stack.pop())

    def peek(self):
        print("top element is",self.stack[-1]) 

    def display(self):
        if len(self.stack)==0:
            print("stack is empty")
        else:
            print(self.stack)

    def reverse(self):
        if len(self.stack)==0:
            print("stack is empty")
        else:
            self.stack=self.stack[::-1]
            print("stack is reversed")
s=stack()
s.push(10)  
s.push(20)
s.push(30)
s.display()
s.reverse()
s.display()''


#copy one stack data to another stack without using linked list
class stack:
    def __init__(self):
        self.stack=[]

    def push(self,item):
        self.stack.append(item)
        print(item,"is pushed")

    def pop(self):
        if len(self.stack)==0:
            print("stack is empty") 
        else:
            print("poped element is",self.stack.pop())

    def peek(self):
        print("top element is",self.stack[-1]) 

    def display(self):
        if len(self.stack)==0:
            print("stack is empty")
        else:
            print(self.stack)

    def copy_stack(self,other_stack):
        other_stack.stack=self.stack.copy()
        print("stack is copied to another stack")

s1=stack()
s1.push(10)     
s1.push(20)
s1.push(30)
s1.display()
s2=stack()
s1.copy_stack(s2)
s2.display()

''


#to check whether the given expression is balanced or not using stack
class stack:
    def __init__(self):
        self.stack=[]

    def push(self,item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack)==0:
            return None
        else:
            return self.stack.pop()

    def peek(self):
        if len(self.stack)==0:
            return None
        else:
            return self.stack[-1]

    def is_empty(self):
        return len(self.stack)==0

    def is_balanced(self,expression):
        for char in expression:
            if char in "({[":
                self.push(char)
            elif char in ")}]":
                if self.is_empty():
                    return False
                top=self.pop()
                if (char==")" and top!="(") or (char=="}" and top!="{") or (char=="]" and top!="["):
                    return False
        return self.is_empty()
s=stack()
expression="{[()()]}"
if s.is_balanced(expression):
    print(expression,"is balanced")     
else:
    print(expression,"is not balanced")''



#convert infix expression to postfix expression
def precedence(op):
    if op=='+' or op == '-':
        return 1
    elif op == '*' or op=='/':
        return 2
    elif op=='^':
        return 3
    return 0
infix=input("enter infix expression")
stack=[]
postfix=""
for ch in infix:
    if ch.isalnum():
        postfix+=ch
    elif ch=='(':
        stack.append(ch)
    elif ch==')':
        while stack and stack[-1]!='(':
            postfix+=stack.pop()
        if stack:
            stack.pop()
    else:
        while stack and precedence(stack[-1])>=precedence(ch):
            postfix+=stack.pop()
        stack.append(ch)
while stack:
    postfix+=stack.pop()
print("postfix expression:",postfix)
''

#Implementation of Dequeue Operation in a queue
queue=list(map(int,input("enter queue elements:").split()))
if len(queue)==0:
    print("Queue Underflow")
else:
    removed=queue.pop(0)
    print("Deleted element",removed)
    print("Updated Queue",queue)
''

# Implementation of enqueue operation in a queue
queue = list(map(int, input("Enter queue elements: ").split()))
element = int(input("Enter element to enqueue: "))
queue.append(element)
print("Updated Queue:", queue)
'''
# Implementation of circular Queue using list
size = int(input("Enter queue size: "))
queue = [0] * size
front = -1
rear = -1

while True:
    print("\n1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")
    choice = int(input("Enter choice: "))
    
    if choice == 1:
        if (rear + 1) % size == front:
            print("Queue Overflow")
        else:
            ele = int(input("Enter element: "))
            if front == -1: 
                front = rear = 0
            else:   
                rear = (rear + 1) % size
            queue[rear] = ele
            print(f"Inserted: {ele}")
            
    elif choice == 2:
        if front == -1:
            print("Queue Underflow")
        else:
            print("Deleted:", queue[front])
            if front == rear: 
                front = rear = -1
            else:
                front = (front + 1) % size
                
    elif choice == 3:
        if front == -1:
            print("Queue is Empty")
        else:
            print("Queue elements are: ", end="")
            i = front
            while True:
                print(queue[i], end=" ")
                if i == rear:
                    break
                i = (i + 1) % size
            print() 
            
    elif choice == 4:
        print("Exiting...")
        break
        
    else:
        print("Invalid choice! Please choose between 1 and 4.")
