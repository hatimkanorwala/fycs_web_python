try:
    num1 = int(input("Enter 1st Number: "))
    num2 = int(input("Enter 2nd Number: "))
    result = num1/num2
except ZeroDivisionError:
    print("Error Cannot Divide any number by Zero")
except ValueError:
    print("Only Integers allowed")
except Exception as e:
    print("Some error occured", e)
else:
    print("Else Block Executed")
finally:
    print("Finally Block Executed")
