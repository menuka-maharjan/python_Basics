import math
a=float(input())
b=float(input())
c=float(input())
d=(b**2)+(4*a*c)
n1=(-b+math.sqrt(d))/(2*a)
n2=(-b-math.sqrt(d))/(2*a)
print("The solutions are:",n1,n2)