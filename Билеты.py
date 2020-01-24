# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 14:16:26 2019

@author: karan
"""
import numpy as np
import sympy as sp
import scipy as sc
from scipy.integrate import odeint 
import IPython.display
#init_printing(use_latex=True)
import matplotlib.pyplot as plt
from scipy.integrate import quad
                                #Bilet 1
''' 
                                #Zad 1 Zadacha Koshi Simvolno i Chislenno
                                # Simvolno
sp.var('C1 C2')
x=sp.symbols('x')
#x=sp.symbols('x')
y=sp.Function('y')
de=sp.Eq(y(x).diff(x,x)-2*y(x).diff(x),(4*sp.exp(-2*x)/(1+sp.exp(-2*x))))
IPython.display.display(de)
rez = sp.dsolve(de,y(x))
IPython.display.display(rez)
eq1=rez.rhs.subs(x,0)
IPython.display.display(eq1)
eq2=rez.rhs.diff(x).subs(x,0)
IPython.display.display(eq2)
seq=sp.solve([eq1-sp.ln(4),eq2-sp.ln(4)+2],C1,C2)
IPython.display.display(seq)
fin=rez.rhs.subs([(C1,seq[C1]),(C2,seq[C2])])
F=sp.Lambda(x,fin)
IPython.display.display(fin)
f=sp.lambdify(x,fin,"numpy")
x=np.linspace(0,5,100)
plt.grid(True)
plt.plot(x,f(x),linewidth=3)
plt.show()
                                # Chislenno
def k(z,x):
    z1,z2 = z
    return [z2,2*z2+4*sc.exp(-2*x)/(1+sc.exp(-2*x))]
t=np.linspace(0,5,100)
z0=[sc.log(4),sc.log(4)-2]
[z1,z2]=odeint(k,z0,t,full_output=False).T
fig=plt.figure()
plt.plot(x,z1,'-o',linewidth=2)
plt.grid(True)
'''
                                #Zad 2 Ploshad figuri Simvolno i Chislenno
                                #Simvolno
x=sp.symbols('x')
y=20-x**2
y1=-8*x
root=sp.solve(y-y1,x)
#print(root)
a=root[0]
b=root[-1]
s=sp.integrate(y-y1,(x,a,b))
print('s=',s)
                                #Chislenno
def f(x):
    return 20-x**2+8*x
I=quad(f,a,b)
print(I)
x=np.linspace(-3,11,300)
f1=20-x**2
f2=-8*x
plt.plot(x,f1,x,f2,linewidth=2)
x=np.linspace(-2,10,300)
f1=20-x**2
f2=-8*x
plt.fill_between(x, f1,f2,color='c')
plt.xlim(-3,11);plt.grid(True)
plt.show()

                               # Zad 3 Elstat potenzial, 2D Contour Graph

