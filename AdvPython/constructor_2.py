class abc:
    def __init__(self,n1,n2):
        self.num1 = n1
        self.num2 = n2
        self.result =0
    def add(self):
        self.result = self.num1 + self.num2
    def subtract(self):
        self.result = self.num1 - self.num2
    def multiply(self):
        self.result = self.num1 * self.num2
    def divide(self):
        self.result = self.num1 / self.num2
    def modulus(self):
        self.result = self.num1 % self.num2
    def display(self):
        print("Result ",self.result)

while True:
    num1 = int(input("Enter 1st Number: "))
    num2 = int(input("Enter 2nd Number: "))
    operation = int(input("Selection operation\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Modulus\nEnter Option"))
    obj = abc(num1,num2)
    if operation == 1:
        obj.add()
    elif operation == 2:
        obj.subtract()
    elif operation == 3:
        obj.multiply()
    elif operation == 4:
        obj.divide()
    elif operation == 5:
        obj.modulus()
    obj.display()
    op = int(input("Press -1 to Exit: "))
    if op == -1:
        break 
