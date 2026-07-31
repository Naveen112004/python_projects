# class Bank:
#     def __init__(self, accno, name, pin, balance=0):
#         self.accno = accno
#         self.name = name
#         self.pin = pin
#         self.balance = balance
#     def __add__(self, amount):
#         self.balance += amount
#         print(f"{self.balance} is deposited to bank")
#     def validate_pin(self, entered_pin):
#         return self.pin == entered_pin
#     def __sub__(self, amount):
#         if self.balance >= amount:
#             self.balance -= amount
#             print(f"{amount} is withdraw from bank")
#             print(f"Total balance:{self.balance}")
#         else:
#             print("Insufficient balance!")
#     def __call__(self):
#         print(f"Account No: {self.accno}, Name: {self.name}, Balance: {self.balance}")
#     def __gt__(self, other):
#         return self.balance > other.balance
#     def __repr__(self):
#         return f"Account No: {self.accno}, Name: {self.name}, Balance: {self.balance}"
# b1 = Bank(992200101, "Naveen", 1234)
# b2 = Bank(992200102, "Karthik", 5678)
#
# b1 + 50000
# if b1.validate_pin(1234):
#     b1 - 35000
# b1()
# l=[b1,b2]
# print(l)
# print(b1 > b2)
