class data:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.result = 0
        print("Print from Constructor of Class Data")
    def getData(self):
        self.num1 = int(input("Enter 1st Number: "))
        self.num2 = int(input("Enter 2nd Number: "))
    def display(self):
        print("Result: ",self.result)
class calculator(data):
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

obj = calculator()
obj.getData()
obj.add()
obj.display()
obj.subtract()
obj.display()
obj.multiply()
obj.display()
obj.divide()
obj.display()
obj.modulus()
obj.display()
