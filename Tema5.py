#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 23:53:16 2019

@author: ihor
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
'''
#Zad 5.1
print('Zad 5.1')
a=np.array(sorted(np.random.randint(0,200,16),reverse=True))
A=a.reshape(4,4)
print(A)
B=np.eye(4)
for i in range(4):
    for j in range(4):
        B[i,j]=5
C=np.eye(4)
for i in range(4):
    for j in range(4):
        C[i,j]=i**2-j**2
D=np.eye(4)
E=np.diag(np.ones(4))
print(A+B-C-D+E-3)
#Zad 5.2
print('Zad 5.2')
x=np.array([-3,0,1,2,5],dtype=np.int16)
y=np.array([-5,0,-4,1,3],dtype=np.int16)
X,Y=np.meshgrid(x,y)
Z=X**2-Y**2
z=np.array([[1,2,3,4,5]],dtype=np.int16)
z=z.transpose()
Z=np.hstack((Z,z))
z=np.ones(6)
x,y=np.vsplit(Z,[1])
Z=np.vstack((x,z))
Z=np.vstack((Z,y))
print(Z)
#Zad 5.3
print('Zad 5.3')
a=np.array([3,2,1])
A=np.array([4,-2,3,1,-1,1])
A=A.reshape(2,3)
print(a+A)
for j in range(len(A[0])):
    for i in range(len(A)):
        A[i][j]=A[i][j]+a[j]
print(A)
#Zad 5.4
print('Zad 5.4')
A=np.eye(5)
j=4
for i in range(len(A)):
    if i>2:
        A[i][j]=-1
    if i<2:
       A[i][j]=1
    j-=1
print(A)
B,C=np.meshgrid(np.linspace(1,5,5),np.linspace(1,5,5))
print(B)
C=C*2
print(C)
D=A+B+C
for i in range(len(D)):
    D[1][i]=1
print(D)
a=[]
for i in range(D.size):
    if i%5==4:
        a=np.append(a,i)
D=np.delete(D,a).reshape(5,4)
Null=np.linspace(0,0,10).reshape(5,2)
D=np.hstack((D,Null))
print(D)
for i in range(len(D)):
    for j in range(len(D[0])):
        if (1<=i<=3)and(3<=j<=5):
            D[i][j]=3
print(D)
#Zad 5.5
print('Zad 5.5')
A=np.hstack((np.r_[-1:1:9j].reshape(3,3),np.r_[-2:3:6j].reshape(3,2)))
for i in range(len(A)):
    for j in range(len(A[0])):    
        if A[i][j]<0:A[i][j]=0
A,B,C=np.vsplit(np.transpose(A),[1,3])
print(A,B,C,sep='\n')
#Zad 5.6
print('Zad 5.6')
A=np.random.randint(-10,10,20)
a=0;S=0;null=0
B=np.sort(A)
for i in range(len(B)):
    if B[i]<0: a+=1;S+=B[i];B[i]=B[i]**2
    if B[i]==0: null+=1
B=np.sort(B)
for i in range(len(A)):
    if A[i]<0: A[i]=0
print(A,B,sep='\n')
#Zad 5.7
print('Zad 5.7')
n=int(input('VVedite kolichestvo elementov : '))
A=np.random.uniform(-5,5,n).round(2)
a=0
for i in range(len(A)):
    if A[i]<0: a=i
S=0
while a<len(A):
    S+=round(A[i])
    a+=1
print(A,a,S,sep='\n')
B=np.sort(A[ : :2])
C=A
for i in range(len(B)):
        C[2*i]=B[i]
print(C)
#Zad 5.8
print('Zad 5.8')
n=int(input('VVedite kolichestvo elementov : '))
A=np.random.uniform(0,10,n)
print(A.argmin(),A.argmax(),sep='\n')
A=np.hstack((A[1 : :2],A[ : :2]))
print(A)
c=(A.argmin(),A.argmax())
S=np.sum(A[min(c):max(c)+1:1])
print(S)
#Zad 5.9
print('Zad 5.9')
a=np.random.randint(1,10,30)
c=[]
for i in range(len(a)):
    b=0
    for j in range(len(c)):
        if a[i]==c[j] : 
            b+=1
    if b==0 :
        c=np.append(c,a[i])
print(a,len(c),sep='\n')
#Zad 5.10
print('Zad 5.10')
n=int(input('Vvedite kolichestvo elemenov:'))
a=np.random.randint(0,10,n)
b=np.random.randint(0,10,n)
A=set(a)
B=set(b)
k=A&B
print(a,b,k,len(k))
#Zad 5.11
print('Zad 5.11')
a=np.random.uniform(0,20,25)
a.shape=(5,5)
s=list(range(5))
for i in range(len(a)):
    s[i]=np.sum(a[i])
print(a,s,sep='\n')
b=[]
b=np.append(b,a)
b.shape=(5,5)
for i in range(len(b)):
    for j in range(int(b.size/len(b))):
        if (j>i)and((len(b)-j-1)>i): b[i][j]=0
for i in range(len(a)):
    a[i][i]=np.average(a[i])
print(a,b,sep='\n')
#Zad 5.12
print('Zad 5.12')
a=np.random.uniform(0,50,25)
a.shape=(5,5)
print(a)
for i in range(len(a)):
    a[i][len(a)-i-1]=(np.max(a[i])+np.min(a[i]))/2
print(a)
s=0
k=0
m=0
for i in range(len(a)):
    if np.sum(a[i])>s : s=np.sum(a[i]);k=i+1
    if np.min(a[i])>m : m=np.min(a[i])
print(a,s,k,m,sep='\n')
#Zad 5.13
print('Zad 5.13')
n=50
a=np.random.uniform(0,n,25)
a.shape=(5,5)
S=[]
K=[]
for i in range(len(a)):
    s=0
    k=0
    for j in range(i+1):
        if a[4-(i-j)][j]>s :s=a[4-(i-j)][j]
        if a[i-j][4-j]>k :k=a[i-j][4-j]
    S.append(s)
    K.append(k)
S=S+K[:4]
print(a)
print(S)
k=0;t=n+1
for i in range(len(a)):
       if np.max(a[i])>k:p0=i;k=np.max(a[i])
       if np.max(a[i])==k: 
           if i>p0 : p0=i
       if np.min(a[i])<t:p1=i;t=np.min(a[i])
       if np.min(a[i])==t: 
           if i>p1 : p1=i
for i in range(len(a)):
    p2=a[p0][i]
    a[p0][i]=a[p1][i]
    a[p1][i]=p2
print(a)
#Zad 5.14
print('Zad 5.14')
A=np.random.uniform(0,100,25).reshape(5,5)
B=np.random.uniform(0,100,25).reshape(5,5)
C=A<B
print(A)
A[A<B]=B[A<B]
print(A)
print(B)
print(C)
#Zad 5.15
print('Zad 5.15')
x=np.linspace(-3,3,200)
y=np.linspace(-3,3,200)
X,Y=np.meshgrid(x,y)
Z=(1-X**2-Y**2)*(4-X**2-Y**2)
Z[Z<0]=0
Z=np.sqrt(Z)
fig=plt.figure()
ax=Axes3D(fig)
ax.plot_surface(X,Y,Z,color='cyan')
plt.show()
#Zad 5.16
print('Zad 5.16')
x=np.linspace(-4,4,1000)
y=np.linspace(-4,4,1000)
X,Y=np.meshgrid(x,y)
Log=X**2+Y**2
F=np.sqrt(Log)
F[(Log>=4)*(Log<9)]=(3-np.sqrt(Log))[(Log>=4)*(Log<9)]
F[(Log>1)*(Log<4)]=(1+np.sqrt(Log)-0.5*Log)[(Log>1)*(Log<4)]
F[Log>9]=0
fig=plt.figure()
ax=Axes3D(fig)
ax.plot_surface(X,Y,F,color='cyan')
plt.show()
'''

