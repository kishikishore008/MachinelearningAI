'''from sympy import*
var('z')
x,y,c=symbols('x,y,c',real=True)
u=exp(x)*(x*cos(y)-y*sin(y))
ux=diff(u,x)
uy=diff(u,y)
f1=ux.subs([(x,z),(y,0)])
f2=uy.subs([(x,z),(y,0)])
w=simplify(integrate(f1,z)-I*integrate(f2,z))+c
print("f(z)=",w)

from sympy import*
var('z')
x,y,c=symbols('x,y,c',real=True)
u=x**3+3*x**2-3*x*y**2-3*y**2+1
ux=diff(u,x)
uy=diff(u,y)
f1=ux.subs([(x,z),(y,0)])
f2=uy.subs([(x,z),(y,0)])
w=simplify(integrate(f1,z)-I*integrate(f2,z))+c
print("f(z)=",w)

from sympy import*
var('z')
x,y,c=symbols('x,y,c',real=True)
u=sin(x)*cosh(y)
ux=diff(u,x)
uy=diff(u,y)
f1=ux.subs([(x,z),(y,0)])
f2=uy.subs([(x,z),(y,0)])
w=simplify(integrate(f1,z)-I*integrate(f2,z))+c
print("f(z)=",w)'''

from sympy import*
var('z,c')
x,y=symbols('x,y',real=True)
v=x**2-y**2+2*x*y-3*x-2*y
vx=diff(v,x)
vy=diff(v,y)
f1=vx.subs([(x,z),(y,0)])
f2=vy.subs([(x,z),(y,0)])
w=expand(integrate(f2,z)+I*integrate(f1,z))+c
print(f'given image part v={v}')
print(f'required analytic function f(z)={w}')


from sympy import*
var('z,c')
x,y=symbols('x,y',real=True)
v=y+exp(x)*cos(y)
vx=diff(v,x)
vy=diff(v,y)
f1=vx.subs([(x,z),(y,0)])
f2=vy.subs([(x,z),(y,0)])
w=expand(integrate(f2,z)+I*integrate(f1,z))+c
print(f'given image part v={v}')
print(f'required analytic function f(z)={w}')

from sympy import*
var('z,c')
x,y=symbols('x,y',real=True)
v=exp(-y)*(x*sin(x)+y*cos(x))
vx=diff(v,x)
vy=diff(v,y)
f1=vx.subs([(x,z),(y,0)])
f2=vy.subs([(x,z),(y,0)])
w=expand(integrate(f2,z)+I*integrate(f1,z))+c
print(f'given image part v={v}')
print(f'required analytic function f(z)={w}')