from sympy import * 
x = symbols('x')
d = diff(cos(x)) 
print (d) 
integ = Integral(sin(x), (x, 0, 20))
print(integ.doit())
integi = Integral(x**2*sqrt(x**3+1), (x, -1, 0))
print (integi.doit()) 
s = Integral((1/x), (x)) 
print (s.doit()) 

