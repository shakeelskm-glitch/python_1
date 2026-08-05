#linked list
'''class node:
    def __init__(self, data):
        self.data = data
        self.next = None
node1 = node(10)
node2= node(20)
node3= node(30)
node1.next = node2
node2.next = node3
print(node1.data)
print(node1.next.data)
print(node1.next.next.data)
#find all the pairs in an array whose sum is equal to a given number
def find_pairs(arr, target_sum):
    pairs = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target_sum:
                pairs.append((arr[i], arr[j]))
    return pairs
print(find_pairs([1, 2, 3, 4, 5], 5))''

#kadane's algorithm
arr = [-2,1,-3,4,-1,2,1,-5,4]
max_sum = arr[0]
current_sum = arr[0]
for i in range(1, len(arr)):
    current_sum = max(arr[i], current_sum + arr[i])
    max_sum = max(max_sum, current_sum)
print(max_sum)''

#two pointers
arr = [1, 2, 3, 4, 5]
left = 0
right = len(arr) - 1
while left < right:
    if arr[left] + arr[right] == 5:
        print(arr[left], arr[right])
        left += 1
        right -= 1
    elif arr[left] + arr[right] < 5:
        left += 1
    else:
        right -= 1
print(arr)''

#two pointers palindrome
arr=input("Enter a string: ")
left=0
right=len(arr)-1
while left<right:
    if arr[left]!=arr[right]:
        print("Not a palindrome")
        break
    left+=1
    right-=1
else:
    print("Palindrome")
''
#rainwater trapping problem
arr=[0,1,0,2,1,0,1,3,2,1,2,1]
n=len(arr)
left_max = [0] * n
right_max = [0] * n

# Fill left_max array
left_max[0] = arr[0]
for i in range(1, n):
    left_max[i] = max(left_max[i - 1], arr[i])

# Fill right_max array
right_max[n - 1] = arr[n - 1]
for i in range(n - 2, -1, -1):
    right_max[i] = max(right_max[i + 1], arr[i])

# Calculate the trapped water
trapped_water = 0
for i in range(n):
    water_l0evel = min(left_max[i], right_max[i])
    trapped_water += max(0, water_level - arr[i])

print("Trapped Water:", trapped_water)''
class node:
    def __init__(self, data):
        self.data = data
        self.next = None
#creating nodes
node1 = node(10)
node2 = node(20)    
node3 = node(30)
#linking nodes
node1.next = node2
node2.next = node3
#traversing the linked list
current = node1
while current is not None:
    print(current.data)
    current = current.next
#inserting a new node at the beginning
new_node = node(5)  
new_node.next = node1''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
ll = LinkedList()
n = int(input("Enter the number of nodes: "))
for _ in range(n):
    data = int(input("Enter node data: "))
    ll.insert(data)
print("Linked List:")
ll.display()
def insert_at_end(self, data):
    new_node = Node(data)
    if not self.head:
        self.head = new_node
        return
    current = self.head
    while current.next:
        current = current.next
    current.next = new_node
n = int(input("Enter the number of nodes to insert at the end: "))
for _ in range(n):
    data = int(input("Enter node data: "))
    ll.insert_at_end(data)
position = int(input("Enter the position to insert the new node: "))
data = int(input("Enter the data for the new node: "))
ll.insert_at_position(position, data)''
def delete_first(self):
        if self.head is None:
            print("Linked list is empty")
            return
        self.head = self.head.next  # move head to next node


    # Delete last node
    def delete_last(self):
        if self.head is None:
            print("Linked list is empty")
            return

        # If only one node
        if self.head.next is None:
            self.head = None
            return

        temp = self.head
        while temp.next.next:
            temp = temp.next

        temp.next = None  # remove last node


    #Delete node with given value
    def delete_value(self, value):
        temp = self.head

        # If head node has the value
        if temp is not None and temp.data == value:
            self.head = temp.next
            return''
# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None

    # INSERT METHOD (this was missing earlier)
    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    # Display method
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")
ll = LinkedList()
n = int(input("Enter the number of nodes: "))
for _ in range(n):
    data = int(input("Enter node data: "))
    ll.insert(data)
print("Linked List:")
ll.display()

    def remove(self, data):
        if self.head is None:
            print("List is empty. Cannot remove.")
            return

        # If head node itself holds the data to be removed
        if self.head.data == data:
            self.head = self.head.next
            return

        # Search for the data to be removed, keep track of the previous node
        current = self.head
        prev = None
        while current and current.data != data:
            prev = current
            current = current.next

        # If data was not present in linked list
        if current is None:
            print(f"Data {data} not found in the list.")
            return

        # Unlink the node from the linked list
        prev.next = current.next
        print(f"Removed {data} from the list.")
ll = LinkedList()
n = int(input("Enter the number of nodes: "))
for _ in range(n):
    data = int(input("Enter node data: "))
    ll.remove(data)
print("Linked List:")
ll.display()

    # Insert node at given position
    def insert_at_position(self, data, pos):
        new_node = Node(data)

        # If position is 1, insert at beginning
        if pos == 1:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head
        for _ in range(pos - 2):
            if temp is None or temp.next is None:
                print(f"Position {pos} is out of bounds.")
                return
            temp = temp.next

        new_node.next = temp.next
        temp.next = new_node
ll = LinkedList()
n = int(input("Enter the number of nodes: "))
for _ in range(n):
    data = int(input("Enter node data: "))
    ll.insert_at_position(data, 1)
print("Linked List:")
ll.display()
    # Delete first node
    def delete_first(self):
        if self.head is None:
            print("Linked list is empty")
            return
        self.head = self.head.next  # move head to next node

ll = LinkedList()
n = int(input("Enter the number of nodes: "))
for _ in range(n):
    data = int(input("Enter node data: "))
    ll.delete_first()
print("Linked List:")
ll.display()
    # Delete last node
    def delete_last(self):
        if self.head is None:
            print("Linked list is empty")
            return

        # If only one node
        if self.head.next is None:
            self.head = None
            return

        temp = self.head
        while temp.next.next:
            temp = temp.next

        temp.next = None  # remove last node

ll = LinkedList()
n = int(input("Enter the number of nodes: "))
for _ in range(n):
    data = int(input("Enter node data: "))
    ll.delete_last()
print("Linked List:")
ll.display()
    #Delete node with given value
    def delete_value(self, value):
        temp = self.head

        # If head node has the value
        if temp is not None and temp.data == value:
            self.head = temp.next
            return

        # Search for the value
        while temp is not None and temp.next is not None:
            if temp.next.data == value:
                temp.next = temp.next.next
                return
            temp = temp.next

        print("Value not found in the list")
ll = LinkedList()
n = int(input("Enter the number of nodes: "))
for _ in range(n):
    data = int(input("Enter node data: "))
    ll.delete_value(data)
print("Linked List:")
ll.display()
    # Search an element
    def search(self, value):
        temp = self.head

        while temp:
            if temp.data == value:
                print(value, "found in the linked list")
                return
            temp = temp.next

        print(value, "not found in the linked list")
ll = LinkedList()
n = int(input("Enter the number of nodes: "))
for _ in range(n):
    data = int(input("Enter node data: "))
    ll.search(data)
print("Linked List:")
ll.display()

        #Reverse linked list (iterative)
    def reverse(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next   # store next node
            current.next = prev        # reverse link
            prev = current             # move prev forward
            current = next_node        # move current forward

        self.head = prev               # update head
ll = LinkedList()
n = int(input("Enter the number of nodes: "))
for _ in range(n):
    data = int(input("Enter node data: "))
    ll.reverse()
print("Linked List:")
ll.display()
    # Count number of nodes
    def count_nodes(self):
        count = 0
        temp = self.head

        while temp:
            count += 1
            temp = temp.next

        print("Number of nodes:", count)
ll = LinkedList()
n = int(input("Enter the number of nodes: "))
for _ in range(n):
    data = int(input("Enter node data: "))
    ll.count_nodes()
print("Linked List:")
ll.display()''
player="virat"
if player=="b":
    print("batsman")
elif player:
    print("not a batsman")
else:
    print("unknown")'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node
    def find_nth_from_end(self, n):
        first = self.head
        second = self.head

        for _ in range(n):
            if not first:
                print("The linked list has fewer than", n, "nodes.")
                return
            first = first.next

        while first:
            first = first.next
            second = second.next

        print("The", n, "th node from the end is:", second.data)
ll = LinkedList()
for i in [10, 20, 30, 40, 50]:
    ll.insert(i)
n = int(input("Enter the value of n: "))
ll.find_nth_from_end(n)
