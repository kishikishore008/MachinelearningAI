from sympy import *
a, b, c, d, z1, z2, z3, z4=symbols ('a,b, c, d, z1, z2, z3, z4', complex=True)
w1, w2, w3, w4=symbols ('w1,w2,w3,w4', complex=True)
Z= [z1, z2, z3, z4]
W= [w1, w2, w3, w4]
w=lambda z : (a*z+b) / (c*z+d)
for i in range (0,len(W)) :
     W[i]=w(Z[i])
c1=W[0]-W[1]
c2=W[2]-W[3]
c3=W[0]-W[3] 
c4=W[2]-W[1]
d1=Z[0]-Z[1] 
d2=Z[2]-Z[3] 
d3=Z[0]-Z[3] 
d4=Z[2]-Z[1]
crW= simplify (factor (c1*c2) /factor (c3*c4))
crZ= simplify (factor (d1*d2) /factor (d3*d4) )
print (f'Cross ratio of (wl,w2,w3,w4) = (crW]')
print (f'Cross ratio of (21, 22, z3, 24) = (crzy')
if crW==crZ:
   print(" Hence Cross ratio preserves Bilinear Transformation")