import matplotlib.pyplot as plt
import numpy as np
import math


class lorenz(object):
    def __init__(self,r):
        self.x, self.y, self.z ,self.t= [1.0], [0.0], [0.0], [0.0]
        self.sigma, self.b, self.dt, self.time=10.0, 8./3., 0.0001, 50
        self.r=r
        self.n=int(self.time/self.dt)
        self.I=range(self.n)
    def calculate(self):
        for i in self.I:
            self.t.append(self.t[-1]+self.dt)           
            self.x.append(self.x[-1]+self.sigma*(self.y[-1]-self.x[-1])*self.dt)
            self.y.append(self.y[-1]+(-self.x[-2]*self.z[-1]+self.r*self.x[-2]-self.y[-1])*self.dt)
            self.z.append(self.z[-1]+(self.x[-2]*self.y[-2]-self.b*self.z[-1])*self.dt)
    def plot_zy(self,_ax):
        _ax.plot(self.y, self.z,label='r='+str(self.r))
    def plot_zx(self,_ax):
        _ax.plot(self.x, self.z,label='r='+str(self.r))        

fig= plt.figure(figsize=(14,7))
ax1 = plt.subplot(121)
ax2 = plt.subplot(122)
'''

comp= lorenz(5)
comp.calculate()
comp.plot_zx(ax1)
comp.plot_zy(ax2)


comp=lorenz(10)
comp.calculate()
comp.plot_zx(ax1)
comp.plot_zy(ax2)

'''
comp=lorenz(25)
comp.calculate()
comp.plot_zx(ax1)
comp.plot_zy(ax2)


ax1.set_title('Phase space plot - z versus x',fontsize=14)
ax1.set_xlabel('x',fontsize=14)
ax1.set_ylabel('z',fontsize=14)
ax1.legend(fontsize=12,loc='best')
ax2.set_title('Phase space plot - z versus y',fontsize=14)
ax2.set_xlabel('y',fontsize=14)
ax2.set_ylabel('z',fontsize=14)
ax2.legend(fontsize=12,loc='best')
plt.show(fig)
