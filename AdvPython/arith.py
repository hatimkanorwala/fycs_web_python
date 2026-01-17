#filename: arith.py
class arithmetic:
    def __init__(self,n1,n2):
        self.num1 = n1
        self.num2 = n2
        self.result = 0
    def add(self):
        self.result = self.num1 + self.num2
        return self.result
    def subtract(self):
        self.result = self.num1 - self.num2
        return self.result
    def multiply(self):
        self.result = self.num1 * self.num2
        return self.result
    def divide(self):
        self.result = self.num1 / self.num2
        return self.result
    def modulus(self):
        self.result = self.num1 % self.num2
        return self.result
