"""class car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

car1 = car("Toyota", "Camry")
car2 = car("Honda", "Civic")
print(car1.brand, car1.model)
print(car2.brand, car2.model)

class book:
    def __init__(self,title,author, pages,price,id):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        self.id = id
book1=book("The Great Gatsby", "F. Scott Fitzgerald", 180, 10.99, 1)
book2=book("To Kill a Mockingbird", "Harper Lee", 281, 7.99, 2)
print(book1.title, book1.author, book1.pages, book1.price, book1.id)
print(book2.title, book2.author, book2.pages, book2.price, book2.id)


#single inheritance
class person:
    def __init__(self,name,age,gender):#__init__ is a constructor which is used to initialize the attributes of the class
        self.name = name#self is a reference to the current instance of the class and is used to access variables that belong to the class
        self.age = age
        self.gender = gender
    def display(self):#display() is a method which is used to display the attributes of the class
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)
class student(person):#student class is inheriting from person class
    def __init__(self,name,age,gender,roll_number,grade):
        super().__init__(name,age,gender)#super() is used to call the constructor of the parent class
        self.roll_number = roll_number
        self.grade = grade
    def show(self):
        print("Roll Number:", self.roll_number)
        print("Grade:", self.grade)
student1 = student("John", 20, "Male", 101, "A")
student1.display()
student1.show()


class vehical:
    def __init__ (self,wheels,engine_type,brand):
        self.wheels = wheels
        self.engine_type = engine_type
        self.brand = brand
    def display(self):
        print("number of wheels=",self.wheels)
        print("Engine Type=",self.engine_type)
        print("Brand=",self.brand)
class car(vehical):
    def __init__(self,wheels,engine_type,brand,colour,price):
        super(). __init__(wheels,engine_type,brand)
        self.colour=colour
        self.price=price
    def show(self):
        print("colour=",self.colour)
        print("price=",self.price)
c=car(4,"220cc","BMW","blue",200000)
c.show()
c.display()


#multiple inheritance
class father:
    def skills(self):
        print("father:driving")
class mother:
    def talent(self):
        print("mother:cooking")
class child(father,mother):
    def interest(self):
        print("child:cricket")
    def display(self):
        self.skills()
        self.talent()
        self.interest()        
c=child()
c.display()

class father:
    def __init__(self):
        print("father")
class mother:
    def __init__(self):
        print("mother")
class child(father,mother):
    def __init__(self):
        father.__init__(self)
        mother.__init__(self)
        print("child")
c=child()

class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display(self):
        print("Name=",self.name)
        print("Salary=",self.salary)
class developer(employee):
    def __init__(self,name,salary,dev_id):
        super().__init__(name,salary)
        self.dev_id=dev_id
    def show(self):
        print("id=",self.dev_id)
class HR(developer):
    def __init__(self,name,salary,dev_id,age):
        super().__init__(name,salary,dev_id)
        self.age=age
    def show1(self):
        print("age=",self.age)
h=HR("shakeel",200000,1234,20)
h.display()
h.show()
h.show1()


class A:
    def __init__(self):
        print("Class A")
class B(A):
    def __init__(self):
        print("Class B")
class C:
    def __init__(self):
        print("class C")
class D(B,C):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        C.__init__(self)
        print("Class D")
d=D()""



class student:
    def __init__(self,name):
        self.name=name
    def display1(self):
        print("Name=",self.name)
class teacher(student):
    def __init__(self,name,t_name):
        super().__init__(name)
        self.t_name=t_name
    def display2(self):
        print("Teacher name=",self.t_name)
class principle():
    def __init__(self,p_name,p_salary):
        self.p_name=p_name
        self.p_salary=p_salary
    def display3(self):
        print("Principle Name=",self.p_name)
        print("Principle Salary",self.p_salary)
class chief(teacher,principle):
    def __init__(self,name,t_name,p_name,p_salary,c_age):
        super().__init__(name,t_name,p_name,p_salary)
        self.c_age=c_age
    def display(self):
        student.display1()
        teacher.display2()
        principle.display3()
        print("Chief Name=",self.c_name)
c=chief("shakeel","sonia","murali",200000,45)
c.display()



#poly
class parent:
    def show(self):
        print("this is parent class")
class child(parent):
    def show(self):
        print("this is child class")
c=child()
c.show()""

class Bird:
    def fly(self):
        print("birds can fly")
class Penguin(Bird):
    def fly(self):
        print("cannot fly")

def fly1(bird):
    bird.fly()

sparrow=Bird()
penguin=Penguin()
fly1(sparrow)
fly1(penguin)
"""


#encapsulation
class bank:
    def __init__(self,balance):
        self.__balance=balance
    def deposit(self,amount):
        self.__balance+=amount
    def get_balance(self):
        print( self.__balance)
account=bank(1000)
account.deposit(500)
account.get_balance()
