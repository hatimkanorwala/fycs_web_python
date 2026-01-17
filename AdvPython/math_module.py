#Math is a filename/classname -> they have methods written inside them
#Here all the methods  inside the math class/module is imported in this file

import math

print(math.sqrt(16))      # 4.0        → square root
print(math.pow(2, 3))     # 8.0        → 2³
print(math.pi)            # 3.141592653589793
print(math.e)             # 2.718281828459045
print(math.sin(math.pi/2))# 1.0        → sine
print(math.cos(0))        # 1.0
print(math.factorial(5))  # 120        → 5! = 120
print(math.gcd(12, 18))   # 6          → greatest common divisor (Python 3.9+)

from math import pi
from math import sqrt
#from math import *
print(pi)
print(sqrt(64))
