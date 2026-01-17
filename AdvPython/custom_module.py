from arith import arithmetic
from inp_out import input_output
obj1 = input_output()
num1,num2 = obj1.getData()
obj2 = arithmetic(num1,num2)
op = int(input("Enter Operation\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Modulus\nSelect Operation: "))
if op == 1:
    result = obj2.add()
    obj1.displayResult("Addition",result)
elif op == 2:
    result = obj2.subtract()
    obj1.displayResult("Subtraction",result)
elif op == 3:
    result = obj2.multiply()
    obj1.displayResult("Multiplication",result)
elif op == 4:
    result = obj2.divide()
    obj1.displayResult("Division",result)
elif op == 5:
    result = obj2.modulus()
    obj1.displayResult("Modulus",result)
else:
    print("Please enter correction operation")

    
