# from sympy import * 
# def f(x):
#     return 3*x-cos(x)-1 
# def g(x):
#     return 3+sin(x) 
# x0=0.5
# step=1 
# while(step<=3):
#      x=x0-(f(x0)/g(x0))
#      print("Iterations=%d, x=%0.3f, f(x)=%0.3f"%(step,x,f(x))) 
#      x0=x
#      step=step+1
# print( '\n The required approximation root is=%0.3f ' %x)


# from sympy import *
# def f(x):
#     return 3*x-cos(x)-1
# def g(x):
#     return 3+sin(x)
# x0=0.5
# step=1
# while(step<=3):
#     x=x0-(f(x0)/g(x0))
#     print("Interation=%d,x=%0.3f, f(x)=%0.3f" %(step,x,f(x)))
#     x0=x
#     step=step+1
# print("\n the required approximation root is =%0.3f"%x)




from sympy import*
def f(x):
    return 3*x-cos(x)-1
def g(x):
    return 3+sin(x)
x0=0.5
step=1
while (step<=3):
    x=x0-(f(x0)/g(x0))
    print("interatin=%d,x=%0.3f,f(x)=%0.3f"%(step,x,f(x)))
    x0=x
    step=step+1
print("root %0.3f"%x)    
