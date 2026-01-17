#Filename :- inp_out.py
class input_output:
    def __init__(self):
        print("Constructor called of Input Output")
    def getData(self):
        self.num1 = int(input("Enter 1st Number: "))
        self.num2 = int(input("Enter 2nd Number: "))
        return self.num1,self.num2
    def displayResult(self,op,result):
        print("Result of ",op , " is ",result)
