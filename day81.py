'''#program to count total number of nodes in a linked list
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

    def count_nodes(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        print("Total number of nodes:", count)

ll = LinkedList()
for i in [10, 20, 30, 40, 50]:
    ll.insert(i)
ll.count_nodes()

#program to delete all nodes containing a specific value in a linked list
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

    def delete_nodes(self, value):
        # Delete all nodes with the specified value
        while self.head and self.head.data == value:
            self.head = self.head.next

        current = self.head
        while current and current.next:
            if current.next.data == value:
                current.next = current.next.next
            else:
                current = current.next

ll = LinkedList()
for i in [10, 20, 30, 40, 50]:
    ll.insert(i)
ll.delete_nodes(30)
ll.count_nodes()  # Count nodes after deletion
''
#program to find maximum and minimum in a linked list
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

    def find_max_min(self):
        if not self.head:
            print("The linked list is empty.")
            return None, None

        max_val = self.head.data
        min_val = self.head.data

        current = self.head
        while current:
            if current.data > max_val:
                max_val = current.data
            if current.data < min_val:
                min_val = current.data
            current = current.next

        print("Maximum value:", max_val)
        print("Minimum value:", min_val)

ll = LinkedList()
for i in [10, 20, 30, 40, 50]:
    ll.insert(i)
ll.find_max_min()
''
#program to swap two nodes without swapping data in a linked list
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

    def swap_nodes(self, key1, key2):
        if key1 == key2:
            return

        prev1 = None
        curr1 = self.head
        while curr1 and curr1.data != key1:
            prev1 = curr1
            curr1 = curr1.next

        prev2 = None
        curr2 = self.head
        while curr2 and curr2.data != key2:
            prev2 = curr2
            curr2 = curr2.next

        if not curr1 or not curr2:
            print("One or both keys not found.")
            return

        if prev1:
            prev1.next = curr2
        else:
            self.head = curr2

        if prev2:
            prev2.next = curr1
        else:
            self.head = curr1

        temp = curr1.next
        curr1.next = curr2.next
        curr2.next = temp
ll = LinkedList()
for i in [10, 20, 30, 40, 50]:
    ll.insert(i)
ll.swap_nodes(20, 40)''

#program to count total number of nodes in a linked list
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

 ''   def count_nodes(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        print("Total number of nodes:", count)
ll = LinkedList()
for i in [10, 20, 30, 40, 50]:
    ll.insert(i)
ll.count_nodes()''

#maximum and minimum in a linked list
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

    def find_max_min(self):
        if not self.head:
            print("The linked list is empty.")
            return None, None

        max_val = self.head.data
        min_val = self.head.data

        current = self.head
        while current:
            if current.data > max_val:
                max_val = current.data
            if current.data < min_val:
                min_val = current.data
            current = current.next

        print("Maximum value:", max_val)
        print("Minimum value:", min_val)
ll = LinkedList()
for i in [10, 20, 30, 40, 50]:
    ll.insert(i)
ll.find_max_min()'''
#program to delete all nodes containing a specific value in a linked list
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

    def delete_nodes(self, value):
        # Delete all nodes with the specified value
        while self.head and self.head.data == value:
            self.head = self.head.next

        current = self.head
        while current and current.next:
            if current.next.data == value:
                current.next = current.next.next
            else:
                current = current.next
ll = LinkedList()
for i in [10, 20, 30, 40, 50]:
    ll.insert(i)
ll.delete_nodes(30)