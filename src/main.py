import random as rn 
import numpy as np
from matplotlib import pyplot as plt

def potential(x):
    return 0.5*(x)**2

def rk4(xmax, N,E,p ):
    h=xmax/N
    x=np.linspace(0,xmax,N+1)
    f=np.zeros(N+1)
    df=np.zeros(N+1)
    if p==1:
        phi=0
        dphi=1
    else:
        phi=1
        dphi=0 
    f[0]=phi
    df[0]=dphi
    for i in range(0,N):
        k1=dphi
        p1=-2*(E-potential(x[i]))*phi
        k2=dphi+0.5*p1*h
        p2=-2*(E-potential(x[i]+0.5*h))*(phi+0.5*k1*h)
        k3=dphi+0.5*p2*h
        p3=-2*(E-potential(x[i]+0.5*h))*(phi+0.5*k2*h)
        k4=dphi+0.5*p3*h
        p4=-2*(E-potential(x[i]+h))*(phi+k3*h)
        phi+=(k1+2*k2+2*k3+k4)*h/6
        dphi+=(p1+2*p2+2*p3+p4)*h/6
        f[i+1]=phi
        df[i+1]=dphi
    plt.plot(x,f)
    plt.plot(x,np.zeros(N+1),'-')
    plt.xlabel('x-axis position')
    plt.ylabel('wavefunction')
    plt.xlim(0,5)
    plt.ylim(-1.16,1.16)
    plt.show()
rk4(5, 100,2.55,0 )



