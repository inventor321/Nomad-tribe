
from sympy import *
from numpy import *
import math
import matplotlib.pyplot as plt

t = linspace(0, 10, 400)
a = t
b = cos(t)
c = a + b

plt.plot(t, a, 'r') # plotting t, a separately 
plt.plot(t, b, 'b') # plotting t, b separately 
plt.plot(t, c, 'g') # plotting t, c separately 
#plt.show()

x, y, z = symbols('x y z')
init_printing(use_unicode=True)
print(solveset(x**2 - x*y, (x, y)))
