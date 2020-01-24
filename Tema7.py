#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 12:49:55 2019

@author: ihor
"""
import numpy as np
import scipy as sc
import math
import matplotlib
import scipy.linalg as la
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Wedge, Polygon, Rectangle
from matplotlib.collections import PatchCollection
'''
#Zad 7.1
print('Zad 7.1')
n=10
y=np.random.uniform(0,10,n)
x=np.array(sorted(np.random.uniform(0,10,n)))
print(x,y,sep='\n')
plt.plot(x,y,linewidth=2)
plt.xlim(-0.1,10.1);plt.ylim(-0.1,10.1);plt.grid(True)
plt.show()    
#Zad 7.2
print('Zad 7.2')
n=500
x=np.linspace(-5,5,n)
y1=np.array([])
y2=np.array([])
y3=np.array([])
for i in range(len(x)):
    y1=np.append(y1,math.sin(x[i])/x[i])
    y2=np.append(y2,x[i]-x[i]**3/6+x[i]**5/120)
    y3=np.append(y3,math.sin(x[i]))
plt.plot(x,y1,linewidth=2)
plt.plot(x,y2,linewidth=2)
plt.plot(x,y3,linewidth=2)
plt.show()
#Zad 7.3
print('Zad 7.3')
n=500
t=np.linspace(-10,10,n)
x=np.array([]);y=np.array([]);x1=np.array([]);y1=np.array([])
for i in range(len(t)):
    x=np.append(x,math.cos(t[i])**5)
    y=np.append(y,math.sin(t[i])**5)    
for i in range(len(t)):
    x1=np.append(x1,t[i]-math.sin(t[i]))
    y1=np.append(y1,1-math.cos(t[i]))
plt.plot(x,y,linewidth=2)
plt.plot(x1,y1,linewidth=2)
plt.show()
#Zad 7.4
print('Zad 7.4')
n=500
t=np.linspace(0,2*np.pi,100)
plt.polar(t,2*np.cos(t),linewidth=2,color='blue')
#Zad 7.5
print('Zad 7.5')
n=500
x=np.linspace(-2,2,n)
y=np.piecewise(x,[x<=0,x>0],[lambda x:1-(x+1)**2,lambda x:(x-1)**2-1])
y1=np.piecewise(x,[x<=-1,np.logical_and(x>-1,x<=0),np.logical_and(x>0,x<=1),x>1],[lambda x:-1-x,lambda x:x*(1+x),lambda x:x*(1-x),lambda x:1-x])
plt.plot(x,y1,linewidth=2)
plt.plot(x,y,linewidth=2)
plt.show()
#Zad 7.6
print('Zad 7.6')
x1=np.linspace(0,2*np.pi,18)
x2=np.linspace(0,2*np.pi,12)
print(x1,x2)
plt.polar(x1,np.ones(len(x1)),'o',markersize=7)
plt.polar(x2,0.5*np.ones(len(x2)),'o',markersize=7)
plt.show()
#Zad 7.7
print('Zad 7.7')
def f(x):
    return math.sin(np.pi*x)
delta=1e-10
n=500
x1=0.6
x=np.linspace(-2,2,n)
y=[f(t) for t in x]
y1=[f(x1)+((f(x1+delta)-f(x1-delta))/(2*delta))*(t-x1) for t in x]
plt.plot(x,y,linewidth=2)
plt.plot(x,y1,linewidth=2)
plt.show()
#Zad 7.8
print('Zad 7.8')
delta=1e-15
n=500
t0=4*np.pi/3
t=np.linspace(-2*np.pi,2*np.pi,n)
def fx(t):
    return (t-math.sin(t))
def fy(t):
    return (1-math.cos(t))
x=[fx(i) for i in t]
y=[fy(i) for i in t]
xt=[fx(t0)+i*(fx(t0+delta)-fx(t0-delta))/(2*delta) for i in t]
yt=[fy(t0)+i*(fy(t0+delta)-fy(t0-delta))/(2*delta) for i in t]
xn=[fx(t0)+i*(fy(t0+delta)-fy(t0-delta))/(2*delta) for i in t]
yn=[fy(t0)-i*(fx(t0+delta)-fx(t0-delta))/(2*delta) for i in t]
plt.plot(x,y,linewidth=2)
plt.xlim(-8,8);plt.ylim(-0.1,3)
plt.plot(xt,yt,linewidth=2)
plt.plot(xn,yn,linewidth=2)
plt.show()
#Zad 7.9
print('Zad 7.9')
n=500
x=np.linspace(-5,5,n)
y=np.linspace(-5,5,n)
def f(x,y):
    return (x**2+y**2)**2-y**2+x**2
X,Y=np.meshgrid(x,y)
Z=f(X,Y)
fig=plt.figure(facecolor='white')
ax1=fig.add_subplot(1,2,1)
ax1.contour(X,Y,Z,30)
ax2=fig.add_subplot(1,2,2)
ax2.contourf(X,Y,Z,30)
#Zad 7.10
print('Zad 7.10')
n=500
x=np.linspace(-3,3,n)
y=np.linspace(-3,3,n)
def F1(x,y):
    return 2-x**2-y**2-np.sqrt((1-x**2)**2+(1-y**2)**2)
def F2(x,y):
    return 2-x+y-abs(x)-abs(x-2*y-abs(x))
X,Y=np.meshgrid(x,y)
Z1=F1(X,Y)
Z2=F2(X,Y)
fig=plt.figure(facecolor='white')
ax1=fig.add_subplot(1,2,1)
ax1.contour(X,Y,Z1,1)
ax1.contour(X,Y,Z2,1)
#Zad 7.11
print('Zad 7.11')
delta=1e-15
n=500
x0=-2;y0=-math.sqrt(20)/3
x=np.linspace(-5,5,n)
y=np.linspace(-5,5,n)
def F(x,y):
    return x**2/9+y**2/4-1
X,Y=np.meshgrid(x,y)
Z=F(X,Y)
def Ft(x,y):
    return (x-x0)*(F(x0+delta,y0)-F(x0-delta,y0))/(2*delta) + (y-y0)*(F(x0,y0+delta)-F(x0,y0-delta))/(2*delta)
def Fn(x,y):
    return (y-y0)*(F(x0+delta,y0)-F(x0-delta,y0))/(2*delta) - (x-x0)*(F(x0,y0+delta)-F(x0,y0-delta))/(2*delta)
Zt=Ft(X,Y)
Zn=Fn(X,Y)
fig=plt.figure(facecolor='white')
ax1=fig.add_subplot(1,2,1)
ax1.contour(X,Y,Z,1)
ax1.contour(X,Y,Zt,1)
ax1.contour(X,Y,Zn,1)
#Zad 7.12
print('Zad 7.12')
delta=1e-2
n=500
x=np.linspace(-5,5,n)
x0=[]
for t in x:
    if abs((t-t**2))<delta:
        x0=np.append(x0,t)
x1=[]
for t in x:
    if t>=x0[0] and t<=x0[1]:
        x1=np.append(x1,t)
y=[t for t in x1]
y1=[t**2 for t in x1]
plt.fill_between(x1,y,y1,color='grey')
#Zad 7.13
print('Zad 7.13')
A=np.ones(64).reshape(8,8)*0
for i in range(8):
    for j in range(8):
        if (i==j): A[i][j]=1
        if (8-j==i) and (i>4): A[i][j]=1
im=plt.pcolor(A)
im.set_cmap('Reds_r')
fig=plt.gcf()
fig.set_facecolor('w')
ax=fig.gca()
ax.axis('equal')
'''
#Zad 7.15
print('Zad 7.15')
fig, ax = plt.subplots()
fig.set_facecolor('white')
patches=[]
polygon=Polygon([[7,19],[12,19],[9.5,22]],facecolor='green')
patches.append(polygon)
rect1=Rectangle((7,16),5,3,facecolor='blue')
patches.append(rect1)
ax.add_patch(rect1)
ax.add_patch(polygon)
ax.set_xlim(6,14)
ax.set_ylim(15.5,23)
