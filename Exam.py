# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 09:10:36 2019

@author: Магистр
"""
import numpy as np
import sympy as sp
import scipy as sc
from scipy.integrate import odeint 
import IPython.display
import matplotlib.pyplot as plt
from scipy.integrate import quad

                #Zad 1 
'''
 # Simvolno
sp.var('C1 C2')
t=sp.symbols('t')
z1=sp.Function('z1')
z2=sp.Function('z2')
z3=sp.Function('z3')
eq1=sp.Eq(z1.diff(t)-z2(t),0)
eq2=sp.Eq(z3.diff(t)-6*z1(t)-4*z3(t)-z2(t),0)
eq3=sp.Eq(z2.diff(t)+z2(t)-z1(t)-z3(t),0)
IPython.display.display(de)
rez = sp.dsolve(eq1,eq2,eq3)
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
'''
    #Chislenno
def k(z,x):
    z1,z2,z3 = z
    return [z2,-z2+z1+z3,6*z1+4*z3+z2]
t=np.linspace(2,5,100)
z0=[-1,0,0]
[z1,z2,z3]=odeint(k,z0,t,full_output=False).T
fig=plt.figure()
plt.plot(t,z1,linewidth=2)
plt.plot(t,z3,linewidth=2)
plt.xlim(0,6);plt.ylim(-80000,1000)
plt.grid(True)
            #Zad 2
x=sp.symbols('x')
fn=x*sp.sqrt(x) 
f=sp.sqrt (1+fn.diff(x)**2)
g=sp.lambdify(x, f , "numpy")
L=quad(g,0,1)
print(L)
fig=plt.figure()
x=np.linspace(-1,2,300)
plt.plot(x,g(x),linewidth=2,color='r')
x=np.linspace(0,1,100)
plt.plot(x,g(x),linewidth=2,color='c')
plt.grid(True)
            #Zad 3
x=np.linspace(0,2*np.pi,18)
t=np.linspace(0,2*np.pi,12)
fig=plt.figure()
plt.polar(x,np.ones(len(x)),'o',color='blue')
plt.polar(t,np.ones(len(t))*0.5,'o',color='blue')