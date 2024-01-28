from sympy import*
x=symbols('x')
f=x**3*exp(-x)
factors=factor(f).as_ordered_factors()
p1=factors[0]
m=p1.as_base_exp()[1]
soln=gamma(m+1)
print(f'the value of integral approximately{soln:.2f}')

from sympy import*
x=symbols('x')
f=x**4*exp(-x)
factors=factor(f).as_ordered_factors()
p1=factors[0]
m=p1.as_base_exp()[1]
soln=gamma(m+1)
print(f'the value of integral approximately{soln:.2f}')


from sympy import*
soln=gamma(7)/(2*gamma(4)*gamma(3))
print("the soln:%.2f"%soln)

from sympy import*
soln=(gamma(3)*gamma(3/2))/gamma(9/2)
print("the soln:%.2f"%soln)

from sympy import*
soln=gamma(-5/2)
print("the soln:%.2f"%soln)

from sympy import*
soln=gamma(9/2)*gamma(-1/2)
print("the soln:%.2f"%soln)