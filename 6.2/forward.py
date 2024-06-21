# from sympy import *
# from numpy import * 
# x=[1.00,1.05,1.10,1.15,1.20,1.25,1.30] 
# y=[1.00,1.0247,1.0488,1.0723,1.0954,1.1180,1.1401] 
# h=0.05;n=len(x)
# d=zeros((n,n+1))
# for i in range(0,n):
#     d[i][0]=x[i]
#     d[i][1]=y[i]
# for i in range(1,n):
#    for j in range(0,n-i): 
#       d[j][i+1]=d[j+1][i]-d[j][i]
# print("\n Forward Difference Table \n") 
# for i in range(n):
#     print(x[i],end="\t") 
#     for j in range(n-i):
#        print(d[i][j+1].round(4),end="\t") 
#     print("")
# sum1=d[0][2]-(1/2)*d[0][3]+(1/3)*d[0][4]-(1/4)*d[0][5]+(1/5)* d[0][6]-(1/6)*d[0][7]
# sum2=d[0][3]-d[0][4]+(11/12)*d[0][5]-(5/6)*d[0][6]+(137/180)* d[0][7]
# print("\n y'(1)=",round((sum1/h),4)) 
# print("\n y''(1)=",round((sum2/(h**2)),4))  



# from sympy import *
# from numpy import *
# x=[1,2,3,4,5,6]
# 
# x=1;h=1;n=len(x)
# d=zeros((n,n+1))
# for i in range (0,)



# from sympy import Symbol
# import numpy as np

# x = [1.00, 1.05, 1.10, 1.15, 1.20, 1.25, 1.30]
# y = [1.00, 1.0247, 1.0488, 1.0723, 1.0954, 1.1180, 1.1401]
# h, n = 0.05, len(x)
# d = np.zeros((n, n + 1))

# d[:, 0], d[:, 1] = x, y
# for i in range(2, n + 1):
#     for j in range(n - i + 1):
#         d[j, i] = d[j + 1, i - 1] - d[j, i - 1]

# print("\nForward Difference Table\n")
# for i in range(n):
#     print("\t".join(f"{d[i, j]:.4f}" for j in range(n - i + 1)))

# sum1 = d[0, 2] - (1/2)*d[0, 3] + (1/3)*d[0, 4] - (1/4)*d[0, 5] + (1/5)*d[0, 6] - (1/6)*d[0, 7]
# sum2 = d[0, 3] - d[0, 4] + (11/12)*d[0, 5] - (5/6)*d[0, 6] + (137/180)*d[0, 7]
# print(f"\n y'(1) = {round(sum1 / h, 4)}")
# print(f"\n y''(1) = {round(sum2 / (h**2), 4)}")


# from sympy import *
# import numpy  as np
# x=[1,2,3,4,5,6]
# y=[1,8,27,64,125,216]
# h,n=1,len(x)
# d= np.zeros((n,n+1))
# print (d)
# d[:,0],d[:,1]=x,y
# print(x,y)
# for i in range(2,n+1):
#     for j in range(n-i+1):
#         d[j,i]=d[j+1,i-1]-d[j,i-1]
#         print(d[j,i])
# print ("\n forward table \n")
# for i in range(n):
#     print("\t".join(f"{d[i,j]:.4f}"for j in range(n-i+1)))


# from sympy import*
# from numpy import*
# x=[1.00,1.05,1.10,1.15,1.20,1.25,1.30]
# y=[1.00,1.0247,1.0488,1.0723,1.0954,1.1180,1.1401] 
# X=1;h=0.5;n=len(x)
# d=zeros((n,n+1))
# for i in (0,n):
#     d[i][0]=x[i]
#     d[i][1]=y[i]
# for i in range (1,n):
#     for j in range (0,n-1):
#         d[j][i]=d[j+1][i]-d[j][i]  

# for i in range(n):
#     print(x[i],end="\t")
#     for j in range(n-1):
#         print(d[i][j+1].round(4),end="\t")


from sympy import*
from numpy import*
x=[1.00,1.05,1.10,1.15,1.20,1.25,1.30] 
y=[1.00,1.0247,1.0488,1.0723,1.0954,1.1180,1.1401] 
h=0.05;n=len(x)
d=zeros((n,n+1))
for i in range(0,n):
    d[i][0]=x[i]
    d[i][1]=y[i]
for i in range(1,n):
    for j in range(0,n-i):
        d[j][i+1]=d[j+1][i]-d[j][i]

for i in range(n):
     print(x[i],end="\t")  
     for j in range(n-i):
         print(d[i][j+1].round(4),end="\t") 
     print("")    
