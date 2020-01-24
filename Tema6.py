# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 10:33:33 2019

@author: Магистр
"""
import numpy as np
import scipy as sc
import math
import scipy.linalg as la
import sympy
import matplotlib.pyplot as plt
'''
#Zad 6.1
print('Zad 6.1')
X=np.array([[3,4,5,1],[0,6,7,2],[1,1,6,3],[4,5,2,4]])
Y=np.eye(4)
for i in range(4):
    Y[i]=sc.misc.factorial(X[i])
Z=np.eye(4)
for i in range(4):
    for j in range(4):
        Z[i][j]=math.exp(X[i][j])
print(Y,Z,sep='\n')
#Zad 6.2
print('Zad 6.2')
a=np.matrix([1,-1,6])
b=np.matrix([-3,2,1]).transpose()
ra=la.norm(a)
rb=la.norm(b)
S=np.dot(a,b)
fi=math.acos(a*b/(ra*rb))
S1=np.cross(a,b.transpose())
S2=np.outer(a,b)
print(ra,rb,S,fi,S1,S2,sep='\n')
#Zad 6.3
print('Zad 6.3')
A=np.array([[1,1,2],[1,3,1],[4,1,1]])
B=np.array([[-1,-1,3],[4,-3,-1],[4,2,1]])
C=la.inv(A)
a=la.det(A)
D=la.solve(A,B)
print(np.dot(A,C),C,a,np.dot(A,B),A*B,np.dot(A,B)-A*B,np.dot(A,D)-B,sep='\n')
#Zad 6.4
print('Zad 6.4')
x=np.matrix([3,-1,4])
A=np.matrix([[0,1,-1],[1,0,0],[1,0,1]])
B=np.matrix([[0,1,0],[0,0,2],[1,0,0]])
y=np.dot(x,np.dot(B,2*A+B))
z=np.dot(x,np.dot(A,B)-np.dot(B,A))
print(y,z,sep='\n')
#Zad 6.5
print('Zad 6.5')
x,y,z=sympy.symbols('x y z')
A=sympy.solve([x+y-z,sympy.Eq(3*x+2*y+z,5),sympy.Eq(4*x-y+5*z,3)],x,y,z)
#B=sympy.solve_linear(sympy.Matrix(([1,1,-1,0],[3,2,1,5],[4,-1,5,3])),x,y,z)
print(A,sep='\n')
#Zad 6.6
print('Zad 6.6')
y0=-1
h=0.01
a=0
b=1
x=np.array([a,])
y=np.array([y0,])
i=0
while (a<=b):
    a=a+h; k=y[i];
    x=np.append(x,a,)
    y=np.append(y,k+h*(math.sin(x[i])-k))
    i+=1
yy=np.array([])
for i in range(len(y)-1):
    yy=np.append(yy,y[i+1]-y[i])
x=np.delete(x,x[-1])
plt.plot(x,yy,'o',markersize=10)
plt.grid(True)
plt.show()
#Zad 6.7
print('Zad 6.7')
n=50
h=1/(n-1)
a0=np.ones(n)*(h+1)
a1=np.ones(n)*(-2-h)
a2=np.ones(n)
a=np.vstack((a0,a1,a2))
a[0][0]=0
a[1][0]=1
a[2][-1]=0
a[0][1]=0
a[1][-1]=1
a[2][-2]=0
print(a)
v=np.ones(n)*(h**2)
v[0]=0
v[n-1]=0
print(v)
y=la.solve_banded((1,1),a,v)
print(y)
xx=np.linspace(0,1,101)
yy=np.array([])
for i in range(len(xx)):
    yy=np.append(yy,(math.e-math.exp(1-xx[i])+xx[i]-math.e*xx[i])/(1-math.e))
plt.plot(xx,yy,'r', linewidth=3)
x=np.linspace(0,1,n)
print(x)
plt.plot(x,y,'o',markersize=7)
plt.grid(True)
plt.show()
'''
#Zad 6.8
print('Zad 6.8')
x=np.array([0,1,2,3,4,5])
y=np.array([-3,1.5,0.5,1,-0.5,0])
A=np.vstack([x,np.ones(len(x))]).transpose()
print(A)
a,b = la.lstsq(A,y)[0]
print(a,b)
plt.plot(x,y,'o',markersize=5)
plt.plot(x,a*x+b,'r',linewidth=3)
plt.xlim(-0.1,5.1);plt.ylim(-3.5,2);plt.grid(True)
plt.show()    