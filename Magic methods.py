# Question 1: Bank Account Operations
# Create a class BankAccount with:
# •	attributes: account_holder, balance
# •	instance method: deposit(amount)
# •	instance method: withdraw(amount)
# Implement these magic methods:
# •	__str__() → display account details
# •	__add__() → add balances of two accounts
# •	__sub__() → subtract balances
# •	__eq__() → compare if two accounts have same balance
# •	__lt__() → check which account has lower balance
# •	__getattribute__() → print a message whenever an attribute is accessed
# •	__setattr__() → prevent setting negative balance

# class BankAccount:
#
#     def __init__(self, account_holder, balance):
#         self.account_holder = account_holder
#         self.balance = balance
#
#     def deposit(self, amount):
#         self.balance += amount
#
#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#         else:
#             print("Insufficient Balance")
#
#     def __str__(self):
#         return f"Account Holder: {self.account_holder}, Balance: {self.balance}"
#
#     def __add__(self, other):
#         return self.balance + other.balance
#
#     def __sub__(self, other):
#         return self.balance - other.balance
#
#     def __eq__(self, other):
#         return self.balance == other.balance
#
#     def __lt__(self, other):
#         return self.balance < other.balance
#
#     # def __getattribute__(self, name):
#     #     print(f"Accessing attribute: {name}")
#     #     return object.__getattribute__(self, name)
#
#     def __setattr__(self, name, value):
#         if name == "balance" and value < 0:
#             print("Negative balance is not allowed!")
#         else:
#             object.__setattr__(self, name, value)
#
#
# acc1 = BankAccount("Naveen", 5000)
# acc2 = BankAccount("Rahul", 3000)
#
# print(acc1)
# print(acc2)
#
# acc1.deposit(1000)
# print(acc1)
#
# acc1.withdraw(2000)
# print(acc1)
#
# print("Total Balance:", acc1 + acc2)
#
# print("Balance Difference:", acc1 - acc2)
#
# print("Equal Balance:", acc1 == acc2)
#
# print("Lower Balance:", acc1 < acc2)
#
# print(acc1.account_holder)
#
# acc1.balance = -500

# Question 2: Product Price Comparison
# Create a class Product with:
# •	attributes: name, price, quantity
# •	method: total_price()
# Implement:
# •	__str__()
# •	__add__() → add total prices of two products
# •	__mul__() → multiply product price by a number
# •	__gt__() → compare which product has greater total value
# •	__eq__() → compare prices
# •	__getattr__() → return "Attribute not found" for missing attributes
# •	__setattr__() → do not allow price less than 0
# ________________________________________

# class Product:
#
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#
#     def total_price(self):
#         return self.price * self.quantity
#
#     def __str__(self):
#         return f"Name:{self.name}, Price:{self.price}, Quantity:{self.quantity}"
#
#     def __add__(self, other):
#         return self.total_price() + other.total_price()
#
#     def __mul__(self, number):
#         return self.price * number
#
#     def __gt__(self, other):
#         return self.total_price() > other.total_price()
#
#     def __eq__(self, other):
#         return self.price == other.price
#
#     def __getattr__(self, name):
#         return "Attribute not found"
#
#     def __setattr__(self, name, value):
#         if name == "price" and value < 0:
#             print("Price cannot be negative")
#         else:
#             object.__setattr__(self, name, value)
#
#
# p1=Product("Laptop",50000,4)
# p2=Product("Phone",30000,6)
# print(p1)
# print(p2)
# print(p1.total_price())
# print(p1+p2)
# print(p1>p2)
# print(p1==p2)
# print(p1.color)
# print(p1.Laptop)
# p1.price=-100


# class Student:
#
#     def __init__(self, roll_no, name, age, course, marks):
#         self.roll_no = roll_no
#         self.name = name
#         self.age = age
#         self.course = course
#         self.marks = marks
#
#     def grade(self):
#         if self.marks >= 90:
#             return "A+"
#         elif self.marks >= 75:
#             return "A"
#         elif self.marks >= 60:
#             return "B"
#         elif self.marks >= 40:
#             return "C"
#         else:
#             return "Fail"
#
#     def is_passed(self):
#         return self.marks >= 40
#
#     def display(self):
#         print("--------------------------------------------")
#         print("Roll No :", self.roll_no)
#         print("Name    :", self.name)
#         print("Age     :", self.age)
#         print("Course  :", self.course)
#         print("Marks   :", self.marks)
#         print("Grade   :", self.grade())
#         print("Passed  :", self.is_passed())
#
#
# students = [
#
# Student(1,"Naveen",21,"CSE",95),
# Student(2,"Ram",20,"ECE",82),
# Student(3,"Ravi",22,"EEE",67),
# Student(4,"Kiran",21,"MECH",55),
# Student(5,"Suresh",20,"CIVIL",38),
#
# Student(6,"Ajay",21,"CSE",91),
# Student(7,"Mahesh",20,"ECE",76),
# Student(8,"Vinay",21,"EEE",48),
# Student(9,"Rahul",22,"CSE",35),
# Student(10,"Arjun",20,"MECH",88),
#
# Student(11,"Karthik",21,"CSE",62),
# Student(12,"Naresh",20,"ECE",71),
# Student(13,"Prasad",22,"EEE",53),
# Student(14,"Ramesh",21,"CIVIL",44),
# Student(15,"Manoj",20,"MECH",99),
#
# Student(16,"Sai",21,"CSE",84),
# Student(17,"Charan",20,"ECE",39),
# Student(18,"Lokesh",21,"EEE",74),
# Student(19,"Teja",22,"CSE",58),
# Student(20,"Harsha",21,"MECH",93)
#
# ]
#
#
# for student in students:
#     student.display()
#
# print("----- Pass Students -----")
# for student in students:
#     if student.marks > 40:
#         print(student.name, student.marks)
#
# print()
#
# print("----- Fail Students -----")
# for student in students:
#     if student.marks < 40:
#         print(student.name, student.marks)
#
# print()
#
# highest = students[0]
#
# for student in students:
#     if student.marks > highest.marks:
#         highest = student
#
# print("Highest Marks :", highest.name, highest.marks)
#
# lowest = students[0]
#
# for student in students:
#     if student.marks < lowest.marks:
#         lowest = student
#
# print("Lowest Marks :", lowest.name, lowest.marks)


# Question 3: Student Marks
# Create a class Student with:
# •	attributes: name, marks
# •	method: grade()
# Implement:
# •	__str__()
# •	__add__() → add marks of two students
# •	__truediv__() → divide marks by a number
# •	__ge__() → check if one student scored greater than or equal to another
# •	__lt__() → check if one student scored less
# •	__getattribute__() → track attribute access
# •	__setattr__() → marks must be between 0 and 100 


# class Student:
#
#     # Constructor
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#
#     # Grade Method
#     def grade(self):
#         if self.marks >= 95:
#             return "A+"
#         elif self.marks >= 90:
#             return "A"
#         elif self.marks >= 80:
#             return "B+"
#         elif self.marks >= 70:
#             return "B"
#         elif self.marks >= 60:
#             return "C"
#         elif self.marks >= 50:
#             return "D"
#         elif self.marks >= 40:
#             return "E"
#         else:
#             return "Fail"
#
#     # String Representation
#     def __str__(self):
#         return f"Name: {self.name}, Marks: {self.marks}, Grade: {self.grade()}"
#
#     # Add Marks
#     def __add__(self, other):
#         return self.marks + other.marks
#
#     # Divide Marks by a Number
#     def __truediv__(self, number):
#         return self.marks / number
#
#     # Greater Than or Equal
#     def __ge__(self, other):
#         return self.marks >= other.marks
#
#     # Less Than
#     def __lt__(self, other):
#         return self.marks < other.marks
#
#     # Track Attribute Access
#     def __getattribute__(self, name):
#         print(f"Accessing attribute: {name}")
#         return object.__getattribute__(self, name)
#
#     # Restrict Marks
#     def __setattr__(self, name, value):
#         if name == "marks" and not (0 <= value <= 100):
#             print("Marks must be between 0 and 100")
#         else:
#             object.__setattr__(self, name, value)
#
#
# # Objects
# student1 = Student("Naveen", 95)
# student2 = Student("Ram", 90)
#
# # __str__()
# print(student1)
# print(student2)
#
# # __add__()
# print("Total Marks:", student1 + student2)
#
# # __truediv__()
# print("Half Marks:", student1 / 5)
#
# # __ge__()
# print("student1 >= student2 :", student1 >= student2)
#
# # __lt__()
# print("student1 < student2 :", student1 < student2)
#
# # __getattribute__()
# print(student1.name)
#
# # __setattr__()
# student1.marks = 150
#
# # Check Value
# print(student1.marks)
#
#
# student1=Student("Naveen",95)
# student2=Student("Ram",90)
#
# print(student1)
# print(student2)
# print(student1+student2)
# print(student1/5)
# print(student1>=student2)
# print(student1<student2)
# print(student1.name)
# student1.marks=150


# Question 4: Rectangle Area Comparison
# Create a class Rectangle with:
# •	attributes: length, breadth
# •	method: area()
# Implement:
# •	__str__()
# •	__add__() → add areas of two rectangles
# •	__sub__() → subtract areas
# •	__eq__() → compare areas
# •	__gt__() → check which rectangle has larger area
# •	__getattr__() → handle missing attributes
# •	__setattr__() → length and breadth must be positive

# class Rectangle:
#     def __init__(self,length,breadth):
#         self.length=length
#         self.breadth=breadth
#
#     def area(self):
#         return self. length * self.breadth
#
#     def __str__(self):
#         return f"Length: {self.length}, Breadth: {self.breadth},Area:{self.area()}"
#
#     def __add__(self,other):
#         return self.area() + other.area()
#
#     def __sub__(self,other):
#         return self.area() - other.area()
#
#     def __eq__(self,other):
#         return self.area() == other.area()
#
#     def __gt__(self,other):
#         return self.area() > other.area()
#
#     def __getattr__(self,name):
#         return  f"{name}Attribute not found"
#
#     def __setattr__(self,name, value):
#         if name in ("length","breadth") and value<=0:
#             print("length and breadth must be positive")
#         else:
#             object.__setattr__(self, name, value)
#
# r1=Rectangle(10,5)
# r2=Rectangle(4,8)
#
# print(r1)
# print(r2)
# print("Total Area:",r1+r2)
# print("Area Difference:",r1-r2)
# print("Equal Area:",r1==r2)
# print(r1>r2)
# print(r1.color)
# r1.length=-10


# Question 5: Employee Salary System
# Create a class Employee with:
# •	attributes: name, salary
# •	method: annual_salary()
# Implement:
# •	__str__()
# •	__add__() → add salaries of two employees
# •	__mul__() → calculate salary after multiplying by months
# •	__ne__() → check if salaries are not equal
# •	__le__() → check if one salary is less than or equal to another
# •	__getattribute__() → log every attribute access
# •	__setattr__() → salary cannot be below 10000


# class Employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#
#     def annual_salary(self):
#         return self.salary * 12
#
#     def __str__(self):
#         return f"name: {self.name}, salary: {self.salary}, Annual_salary:{self.annual_salary()}"
#
#     def __add__(self,other):
#         return self.salary + other.salary
#
#     def __mul__(self,other):
#         return self.salary * 12
#
#     def __ne__(self,other):
#         return self.salary != other.salary
#
#     def __le__(self,other):
#         return self.salary <= other.salary
#
#     def __getattribute__(self, name):
#         print(f"Accessing attribute: {name}")
#         return object.__getattribute__(self, name)
#
#     def __setattr__(self,name,value):
#         if name == "salary" and not (0 <= value < 10000):
#             print(" Invalid salary")
#         else:
#             object.__setattr__(self, name, value)
#
#
# emp1=Employee("Naveen",75000)
# emp2=Employee("Arjun",80000)
#
# print(emp1)
# print(emp2)
# print(emp1+emp2)
# print(emp1*12)
# print(emp1!=emp2)
# print(emp1<=emp2)
# print(emp1.name)
# emp1.salary=80000



#practice
# class Mobile:
#     def __init__(self,brand ,price):
#         self.brand=brand
#         self.price=price
#
#
#
# m1=Mobile("Samsung",80000)
# m2=Mobile("Apple",90000)
#
# print(m1.brand)
# print(m1.price)
# print(m2.brand)
# print(m2.price)
