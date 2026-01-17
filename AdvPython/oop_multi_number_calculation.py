class abc:
    def __init__(self):
        self.num = []
        self.result = 0
        self.total = 0
    def getTotalInput(self):
        self.total = int(input("Enter total numbers: "))
    def getData(self):
        for i in range(1,self.total+1):
            self.n = int(input("Enter Number: "))
            self.num.append(self.n)
    def add(self):
        for i in self.num:
            self.result = self.result + i
    def subtract(self):
        for i in self.num:
            self.result = self.result - i
    def multiply(self):
        for i in self.num:
            self.result = self.result * i
    def display(self):
        print("Result: ",self.result)
while True:
    operation = int(input("1.Addition\n2.Subtraction\n3.Multiplication\nSelection Operation: "))
    obj = abc()
    obj.getTotalInput()
    obj.getData()
    if operation == 1:
        obj.add()
    elif operation == 2:
        obj.subtract()
    elif operation == 3:
        obj.multiply()
    obj.display()
    op = int(input("Enter -1 to Exit"))
    if op == -1:
        break
