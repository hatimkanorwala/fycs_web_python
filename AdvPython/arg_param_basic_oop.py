class calculation:
    def getData(self,n1,n2):
        self.num1 = n1
        self.num2 = n2
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

num1 = int(input("Enter 1st Number: "))
num2 = int(input("Enter 2nd Number: "))
obj = calculation()
obj.getData(num1,num2)
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
