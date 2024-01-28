from sympy import*
x,y=symbols('x,y',real=True)
u=exp(x)*cos(y)+x*y
uxx=diff(u,x,2);uyy=diff(u,y,2)
if simplify(uxx+uyy)==0:
    print("given function is harmonis")    
else:
    print("given function is not a harmonic")

from sympy import*
x,y=symbols('x,y',real=True)
u=exp(-x)*x*sin(y)-exp(-x)*y*cos(y)
uxx=diff(u,x,2);uyy=diff(u,y,2)
if simplify(uxx+uyy)==0:
    print("given function is harmonis")    
else:
    print("given function is not a harmonic")

from sympy import*
x,y=symbols('x,y',real=True)
u=exp(x)*sin(y)+x**2-y**2
uxx=diff(u,x,2);uyy=diff(u,y,2)
if simplify(uxx+uyy)==0:
    print("given function is harmonis")    
else:
    print("given function is not a harmonic")

from sympy import*
x,y=symbols('x,y',real=True)
u=1/2*log(x**2+y**2); v=2*x*y
uxx=diff(u,x,2);vxx=diff(u,x,2)
uyy=diff(u,y,2);vyy=diff(u,y,2)
if simplify(uxx+uyy)==0 and simplify(vxx+vyy)==0:
    print("given function is harmonis")    
else:
    print("given function is not a harmonic")


from sympy import*
r,t=symbols('r,t',real=True)
u=r*sin(t)+cos(t)/r
ur=diff(u,r); urr=diff(u,r,2);utt=diff(u,t,2)
if simplify(urr+(1/r)*ur+(1/(r**2))*utt)==0:
    print("given function is harmonis")    
else:
    print("given function is not a harmonic")

from sympy import*
r,t=symbols('r,t',real=True)
u=r**2*cos(2*t)-r*sin(t)
ur=diff(u,r); urr=diff(u,r,2);utt=diff(u,t,2)
if simplify(urr+(1/r)*ur+(1/(r**2))*utt)==0:
    print("given function is harmonis")    
else:
    print("given function is not a harmonic")








