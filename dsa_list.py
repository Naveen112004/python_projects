#1
# n = int(input("Enter number of elements: "))
#
# lst = []
#
# for i in range(n):
#     value = input("Enter element: ")
#     lst.append(value)
# print("List:", lst)

#2
# l= input("Enter list: ").split()

# l=list(map(int,input("Enter list:").split()))
# n=int(input("Enter element:"))
# i=int(input("Enter index:"))
# l.insert(i,n)
# print(l)

#3

# l1=[10,20,30,40]
# l2=[50,60,70,80]
# l1.extend(l2)
# print(l1)

#4
# l=[10,15,20,30]
# n=int(input("Enter a number:"))
# if(n in l):
#     l.remove(n)
#     print(l)
# else:
#     print("Invalid")

#5
# l=[10,20,25,30,40,]
# i=int(input("Enter index:"))
# n=l.pop(i)
# print(n)

#6
l=[10,20,30,40,50]
n=int(input("Enter a number:"))
if(n in l):
    i=l.index(n)
    print(i)
else:
    print("Invalid")
