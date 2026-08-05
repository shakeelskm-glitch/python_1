'''class student:
    def studentinfo(self):
        self.name=(input("enter student name:"))
        self.rollno=int(input("enter roll number:"))
    def display(self):
        print("Student name=",self.name)
        print("student Roll number=",self.rollno)
class subject(student):
    def subs(self):
        self.s1=int(input("Enter subject1 marks="))
        self.s2=int(input("Enter subject2 marks="))
        self.s3=int(input("Enter subject3 marks="))
    def show(self):
        self.display()
        print("Maths Marks=",self.s1)
        print("Physics Marks=",self.s2)
        print("Chemistry Marks=",self.s3)
class Gradecal(subject):
    def cal(self):
        self.avg= (self.s1+self.s2+self.s3)/3
        print("Average Marks=",self.avg)
        if self.avg>=90:
            print("Grade A")
        elif self.avg>=75:
            print("Grade B")
        elif self.avg>=65:
            print("Grade C")
        elif self.avg>=35:
            print("Pass")
        else:
            print("Fail")
class report(Gradecal):
    def card(self):
        print("***Report Card***")
        print("Student Name:",self.name)
        print("Student Rollno:",self.rollno)
        print("Maths Marks=",self.s1)
        print("Physics Marks=",self.s2)
        print("Chemistry Marks=",self.s3)
        self.cal()
        percentage=self.avg
        print("Percentage=",percentage)
        if percentage>=75:
            print("Very Good")
        else:
            print("Work Hard")

s=report()
s.studentinfo()
s.subs()
s.show()
s.card()
'''

class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True

    def display(self):
        status = "Available" if self.available else "Issued"
        print(f"{self.book_id}\t{self.title}\t{self.author}\t{status}")


class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self):
        book_id = int(input("Enter Book ID: "))
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")

        book = Book(book_id, title, author)
        self.books.append(book)
        print("Book Added Successfully!\n")

    def add_member(self):
        member_id = int(input("Enter Member ID: "))
        name = input("Enter Member Name: ")

        member = Member(member_id, name)
        self.members.append(member)
        print("Member Added Successfully!\n")

    def display_books(self):
        if len(self.books) == 0:
            print("No Books Available.\n")
            return

        print("\nID\tTitle\tAuthor\tStatus")
        print("-" * 40)

        for book in self.books:
            book.display()

        print()

    def issue_book(self):
        book_id = int(input("Enter Book ID to Issue: "))

        for book in self.books:
            if book.book_id == book_id:
                if book.available:
                    book.available = False
                    print("Book Issued Successfully!\n")
                else:
                    print("Book Already Issued.\n")
                return

        print("Book Not Found.\n")

    def return_book(self):
        book_id = int(input("Enter Book ID to Return: "))

        for book in self.books:
            if book.book_id == book_id:
                if not book.available:
                    book.available = True
                    print("Book Returned Successfully!\n")
                else:
                    print("Book was not Issued.\n")
                return

        print("Book Not Found.\n")

    def search_book(self):
        title = input("Enter Book Title: ").lower()

        found = False

        for book in self.books:
            if book.title.lower() == title:
                book.display()
                found = True

        if not found:
            print("Book Not Found.\n")


library = Library()

while True:
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. Add Member")
    print("3. Display Books")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Search Book")
    print("7. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        library.add_book()

    elif choice == 2:
        library.add_member()

    elif choice == 3:
        library.display_books()

    elif choice == 4:
        library.issue_book()

    elif choice == 5:
        library.return_book()

    elif choice == 6:
        library.search_book()

    elif choice == 7:
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")