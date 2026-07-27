# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#
#     def is_passed(self):
#         return self.marks >45
#
#     def grade(self):
#         if self.marks>=90:
#             return "A"
#         elif self.marks>=80:
#             return "B"
#         elif self.marks>=70:
#             return "C"
#         elif self.marks>=60:
#             return "D"
#         elif self.marks>=50:
#             return "E"
#         elif self.marks>=40:
#             return "F"
#         else:
#             return "F"
#
#
# student1 = Student("Alice", 75)
# student2 = Student("Bob", 35)
# student3 = Student("Babu",90)
# student4 = Student("Ram", 56)
# student5 = Student("jill ", 96)
# student6 = Student("jilll", 87)
# student7 = Student("jiga", 58)

###for all objects
# for student in [student1, student2,student3,student4,student5,student6,student7]:
#     if student.is_passed():
#         print(f"{student.name} has passed.")
#     else:
#         print(f"{student.name} has failed.")
#
#     print("Grade",student.grade())

###for only one student
# if student7.is_passed():
#     print(f"{student7.name} has passed.")
# else:
#     print(f"{student7.name}has failed")
#
# print("Grade",student7.grade())



# class Employee:
#
#     company_name = "o:o:o"
#
#     def __init__(self, name):
#         self.name = name

    # @classmethod
    # def change_company(cls, new_name):
    #     cls.company_name = new_name


# emp1 = Employee("Naveen")
# emp2 = Employee("Arjun")
#
# print(emp1.name, emp1.company_name)
# print(emp2.name, emp2.company_name)

# Employee.change_company("CHATGPT")
#
# print(emp1.name, emp1.company_name)
# print(emp2.name, emp2.company_name)

# class Cart:
#     def __init__(self):
#         self.l = []
#
#     def __add__(self, item):
#         self.l.append(item)
#         return self
#
#     def __sub__(self, item):
#         if item in self.l:
#             self.l.remove(item)
#         else:
#             print(item, "not found")
#         return self
#
#     def __str__(self):
#         return str(self.l)
#
#
# c1 = Cart()
#
# c1 = c1 + "chips" + "Milkshake" + "Thumpsup"
# c1 = c1 - "Milkshake" - "Chips" - "bingo"
#
# print(c1)




# class Student:
#
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#
#     def display(self):
#         print("Name :", self.name)
#         print("Marks :", self.marks)
#
#
# student1 = Student("Naveen", 95)
# student2= Student("Raju", 89)
#
# student1.display()
# student2.display()


# class Bank:
#
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#
#     def deposit(self, amount):
#         self.balance = self.balance + amount
#
#     def display(self):
#         print(self.name)
#         print(self.balance)
#
#
# customer1 = Bank("Naveen", 1000)
#
# customer1.display()
#
# customer1.deposit(500)
#
# customer1.display()


# class Student:
#
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#
#     def display(self):
#         print("Name :", self.name)
#         print("Marks :", self.marks)
#
# s1 = Student("Naveen", 95)
# s2 = Student("Rahul", 70)
# s3 = Student("Sai", 40)
#
# s1.display()
# print("----------")
# s2.display()
# print("----------")
# s3.display()


