class calculator:
    def getData(self):
        self.num1 = int(input("Enter Number: "))
    def calculate(self):
        for i in range(1,11):
            print(self.num1 , " x ", i , " = " , (self.num1*i))
obj = calculator()
obj.getData()
obj.calculate()
            
