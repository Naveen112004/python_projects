# PYTHON OOP - CLASS AND OBJECT

# 1. Student Class
class Student:
    def __init__(self, name, age, branch):
        self.name = name
        self.age = age
        self.branch = branch


student1 = Student("Naveen", 21, "ECE")
student2 = Student("Arjun", 21, "CSE")

print("Student 1:")
print(student1.name)
print(student1.age)
print(student1.branch)

print()

print("Student 2:")
print(student2.name)
print(student2.age)
print(student2.branch)



# 2. Bank Account Class


class BankAccount:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance


a1 = BankAccount("Naveen", 12345, 70000)

print()
print("Bank Account:")
print(a1.name)
print(a1.account_number)
print(a1.balance)



# 3. Employee Class - Instance Variables


class Employee:
    def __init__(self, name, salary, company, location):
        self.name = name
        self.salary = salary
        self.company = company
        self.location = location


e1 = Employee("Naveen", 70000, "Accenture", "HYD")

print()
print("Employee:")
print(e1.name)
print(e1.salary)
print(e1.company)
print(e1.location)



# 4. Employee Class - Methods


class EmployeeDetails:
    def __init__(self, name, salary, company, location):
        self.name = name
        self.salary = salary
        self.company = company
        self.location = location

    def introduce(self):
        print("My Name is:", self.name)
        print("My Salary is:", self.salary)
        print("I work at:", self.company)
        print("My location is:", self.location)

    def annual_salary(self):
        print("Annual Salary:", self.salary * 12)


e1 = EmployeeDetails("Naveen", 70000, "Accenture", "Hyd")
e2 = EmployeeDetails("Karthik", 60000, "Infosys", "Hyd")
e3 = EmployeeDetails("Arjun", 80000, "TCS", "Bangalore")

print()
e1.introduce()
e1.annual_salary()

print()
e2.introduce()
e2.annual_salary()

print()
e3.introduce()
e3.annual_salary()



# 5. print() vs return


def add_with_print(a, b):
    print(a + b)


add_with_print(10, 20)


def add_with_return(a, b):
    return a + b


result = add_with_return(10, 20)
print("Returned Result:", result)
print("Result + 25:", result + 25)



# 6. Class Variable


class CollegeStudent:
    college = "Kalasalingam University"

    def __init__(self, name, branch):
        self.name = name
        self.branch = branch


s1 = CollegeStudent("Naveen", "ECE")
s2 = CollegeStudent("Arjun", "ECE")

print()
print("College Student 1:")
print(s1.name)
print(s1.branch)
print(s1.college)

print()
print("College Student 2:")
print(s2.name)
print(s2.branch)
print(s2.college)



# 7. Instance Attribute Override


s1.college = "ABC University"

print()
print("After changing s1 college:")

print("s1 college:", s1.college)
print("s2 college:", s2.college)



# 8. return with Object Method


class SalaryEmployee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def annual_salary(self):
        return self.salary * 12


employee = SalaryEmployee("Naveen", 70000)

result = employee.annual_salary()

print()
print("Salary Employee:")
print("Name:", employee.name)
print("Annual Salary:", result)

bonus = 5000

total = result + bonus

print("Annual Salary + Bonus:", total)