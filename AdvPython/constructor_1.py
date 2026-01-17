class abc:
    def __init__(self,n1,n2):
        self.num1 = n1
        self.num2 = n2
        self.result =0
    def add(self):
        self.result = self.num1 + self.num2
    def display(self):
        print("Result ",self.result)


num1 = int(input("Enter 1st Number: "))
num2 = int(input("Enter 2nd Number: "))
obj = abc(num1,num2)
obj.getData()
obj.add()
obj.display()
