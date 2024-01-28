from sympy import *
a, b, c, d, z1, z2, z3, z=symbols ('a,b, c, d, z1, z2, z3, z', complex=True)
w1, w2, w3, w=symbols ('w1,w2,w3,w', complex=True)
Z= [1,1j,-1,z]
W= [1j,0,-1j,w]

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
eq=Eq(crW,crZ)
soln=solve(eq,w)
pprint(soln[0])