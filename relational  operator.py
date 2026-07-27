class Bank:
    def __init__(self,name,acc):
        self.name=name
        self.acc=acc
        self.bal=0
    def __hash__(self):
        return hash(self.acc)
b1=Bank("Naveen",2000)
b2=Bank("Ram",3000)
k={b1,b2}
print(b1==b2)