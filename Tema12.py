# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 10:18:23 2019

@author: Магистр
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad
from scipy.integrate import cumtrapz
from scipy. integrate import dblquad
from scipy.integrate import nquad
import math
'''
#Zad 12.1
print('Zad 12.1')
def f(x):
    return x/(np.sqrt(np.sqrt(x**2+1)))
I=quad(f,1,2)
print(I)
x=np.linspace(0,3,300)
y=f(x)
y1=f(x)
for i in range(len(x)):
    if (x[i] > 1) and (x[i] < 2):
        y1[i]=0
plt.fill_between(x, y,y1,color='c')
plt.xlim(-0,3);plt.grid(True)
plt.show()
#Zad 12.2
print('Zad 12.2')
def f(x):
    return np.exp(-x**2)*np.sin(4*x)**2
x=np.linspace(-3,3,300)
y=f(x)
I=cumtrapz(y,x,initial=0)
plt.plot(x,I)
plt.show()
#Zad 12.3
print('Zad 12.3')
def f(x,y):
    return(12*x**2*y**2+16*x**3*y**3)
g=lambda x: x**2
t=lambda x: -math.sqrt(x)
I=dblquad(f,0,1,t,g)    
print(I)
def ybounds(x):
    return [-math.sqrt(x),x**2]
def xbounds():
    return [0, 1]
I1=nquad(lambda y,x: f(x,y),[ybounds, xbounds])
print(I1)
'''
#Zad 12.4
print('Zad 12.4')
def f(x,y):
    return(1/(x**2+y**2+1))
def k(x):
    return np.sqrt(1-x**2)
def g(x):
    return 0
I=dblquad(f,-1,1,k,g)  
print(I)
def ybounds(x):
    return [k(x),g(x)]
def xbounds():
    return [-1, 1]
I1=nquad(lambda y,x: f(x,y),[ybounds, xbounds])
print(I1)
x=np.linspace(-2,2,300)
y=np.linspace(-2,2,300)

X,Y=np.meshgrid(x,y)
Z=f(X,Y)
fig=plt.figure(facecolor='white')
ax1=fig.add_subplot(1,2,1)
ax1.contour(X,Y,Z,1)
plt.show()
plt.fill_between(x, y,y1,color='c')