# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 12:15:50 2019

@author: Foton
"""
#import mpmath
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
'''
#Zad 8.1
print('Zad 8.1')
fig=plt.figure()
ax=Axes3D(fig)
t=np.linspace(0,8*np.pi,500)
x=np.cos(t)
y=np.sin(t)
z=t/8
ax.plot(x,y,z,linewidth=3)
#Zad 8.2
print('Zad 8.2')
fig=plt.figure()
ax = plt.axes(projection='3d')
u=np.linspace(-np.pi,np.pi,50)
X,Y=np.meshgrid(u,u)
Z=np.sin(X)*np.sin(Y)*(X**2+Y**2)
ax.plot_wireframe(X, Y, Z, rstride=1, cstride=1)
#Zad 8.3
print('Zad 8.3')
x=np.linspace(-3,3,200)
y=np.linspace(-3,3,200)
fig=plt.figure()
ax=plt.axes(projection='3d')
X,Y=np.meshgrid(x,y)
Log=X**2+Y**2
Z=np.sqrt(4-Log)
Z[Log>=4]=0
Z[(Log<=1)*(Log>=0)]=(Log*np.sqrt(3))[(Log<=1)*(Log>=0)]
ax.plot_surface(X,Y,Z,rstride=1,cstride=1,color='w')
#Zad 8.4
print('Zad 8.4')
R=3;r=1
tau=np.linspace(0,2*np.pi,200)
fi=np.linspace(0,2*np.pi,200)
fig=plt.figure()
ax=plt.axes(projection='3d')
TAU, FI = np.meshgrid(tau,fi)
x,y,z=(R+r*np.cos(FI))*np.cos(TAU),(R+r*np.cos(FI))*np.sin(TAU),r*np.sin(FI)
ax.plot_surface(x,y,z,rstride=2,cstride=1)
ax.azim,ax.elev=160,45
f=lambda t, f: [(R+r*mpmath.cos(f)*mpmath.cos(t)),((R+r*mpmath.cos(f))*mpmath.sin(t)),r*mpmath.sin(f)]
mpmath.splot(f,[0,mpmath.pi*2],[0,mpmath.pi*2])
#Zad 8.5
print('Zad 8.5')
R=3;h=2;n=1
u=np.linspace(0,np.pi*2,100)
v=np.linspace(-h/2,h/2,100)
x=lambda u,v:(R+v*np.cos(n*u)/2)*np.cos(u)
y=lambda u,v:(R+v*np.cos(n*u/2))*np.sin(u)
z=lambda u,v:v*np.sin(n*u/2)
U,V=np.meshgrid(u,v)
X,Y,Z=x(U,V),y(U,V),z(U,V)
fig=plt.figure()
ax=plt.axes(projection='3d')
ax.plot_surface(X,Y,Z,rstride=2,cstride=1)
ax.azim,ax.elev=30,30
'''
#Zad 8.6
print('Zad 8.6')
a=3;b=2;c=1
fig=plt.figure()
# Elipsoid
ax=fig.add_subplot(2,2,1,projection='3d')
U=np.linspace(0,np.pi*2,100)
V=np.linspace(-np.pi/2,np.pi/2,100)
u,v=np.meshgrid(U,V)
x,y,z=(a*np.cos(u))*np.cos(v),(b*np.sin(u))*np.cos(v),c*np.sin(v)
ax.plot_surface(x,y,z)
xlocs =np.linspace(-3,3,7) 
ax.set_xticks(xlocs, minor = False)
ylocs =np.linspace(-2,2,5) 
ax.set_yticks(ylocs, minor = False)
zlocs =np.linspace(-1,1,3) 
ax.set_zticks(zlocs, minor = False)
ax.azim,ax.elev=160,45
# Giperboloid
ax=fig.add_subplot(2,2,2,projection='3d')
U=np.linspace(0,np.pi*2,100)
V=np.linspace(-10,10,100)
u,v=np.meshgrid(U,V)
x,y,z=(a*np.cos(u))*np.cosh(v),(b*np.sin(u))*np.cosh(v),c*np.sinh(v)
ax.plot_wireframe(x,y,z,color='k')
xlocs =np.linspace(-2,2,3) 
ax.set_xticks(xlocs*10000, minor = False)
ylocs =np.linspace(-2,2,3) 
ax.set_yticks(ylocs*10000, minor = False)
zlocs =np.linspace(-1,2,4) 
ax.set_zticks(zlocs*10000, minor = False)
ax.azim,ax.elev=160,45
# Tor
R=3;r=1
ax=fig.add_subplot(2,2,3,projection='3d')
tau=np.linspace(0,2*np.pi,200)
fi=np.linspace(0,2*np.pi,200)
TAU, FI = np.meshgrid(tau,fi)
x,y,z=(R+r*np.cos(FI))*np.cos(TAU),(R+r*np.cos(FI))*np.sin(TAU),r*np.sin(FI)
ax.plot_surface(x,y,z)
ax.azim,ax.elev=160,45
xlocs =np.linspace(-4,4,5) 
ax.set_xticks(xlocs, minor = False)
ylocs =np.linspace(-4,4,5) 
ax.set_yticks(ylocs, minor = False)
zlocs =np.linspace(-1,1,3) 
ax.set_zticks(zlocs, minor = False)
# Something
ax=fig.add_subplot(2,2,4,projection='3d')
t=np.linspace(0,8*np.pi,500)
x=np.cos(t)
y=np.sin(t)
z=t/8
ax.plot(x,y,z,linewidth=3)
ax.azim,ax.elev=160,45
xlocs =np.linspace(-1,1,3) 
ax.set_xticks(xlocs, minor = False)
ylocs =np.linspace(-1,1,3) 
ax.set_yticks(ylocs, minor = False)
zlocs =np.linspace(-0,4,3) 
ax.set_zticks(zlocs, minor = False)