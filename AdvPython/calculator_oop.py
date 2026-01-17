class calculation:
    def getData(self):
        self.num1 = int(input("Enter 1st Number: "))
        self.num2 = int(input("Enter 2nd Number: "))
        self.result = 0
    def add(self):
        self.result = self.num1 + self.num2
    def subtract(self):
        self.result = self.num1 - self.num2
    def multiplication(self):
        self.result = self.num1 * self.num2
    def division(self):
        self.result = self.num1 / self.num2
    def modulus(self):
        self.result = self.num1 % self.num2
    def display(self):
        print("Result: ",self.result)

obj = calculation()
obj.getData()
op = int(input("Select Operation\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Modulus\n.Select Operator"))
if(op == 1):
    obj.add()
elif op == 2:
    obj.subtract()
elif op == 3:
    obj.multiplication()
elif op == 4:
    obj.division()
elif op == 5:
    obj.modulus()
else:
    print("Please select Correct Option")
obj.display()
