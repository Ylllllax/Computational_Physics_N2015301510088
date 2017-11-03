import matplotlib.pyplot as plt
import numpy as np
import math


class lorenz(object):
    def __init__(self,r):
        self.x, self.y, self.z ,self.t= [1.0], [0.0], [0.0], [0.0]
        self.sigma, self.b, self.dt, self.time=10.0, 8./3., 0.0001, 30
        self.r=r
        self.n=int(self.time/self.dt)
        self.I=range(self.n)
    def calculate(self):
        for i in self.I:
            self.t.append(self.t[-1]+self.dt)           
            self.x.append(self.x[-1]+self.sigma*(self.y[-1]-self.x[-1])*self.dt)
            self.y.append(self.y[-1]+(-self.x[-2]*self.z[-1]+self.r*self.x[-2]-self.y[-1])*self.dt)
            self.z.append(self.z[-1]+(self.x[-2]*self.y[-2]-self.b*self.z[-1])*self.dt)
    def plot_z(self,_ax):
        _ax.plot(self.t, self.z,label='r='+str(self.r))

fig= plt.figure(figsize=(20,8))
ax1 = plt.subplot(121)

'''
comp= lorenz(160)
comp.calculate()
comp.plot_z(ax1)

'''
comp=lorenz(163.8)
comp.calculate()
comp.plot_z(ax1)


ax1.set_title('Lorenz model - z versus time',fontsize=14)
ax1.set_xlabel('time',fontsize=14)
ax1.set_ylabel('z',fontsize=14)
ax1.legend(fontsize=12,loc='best')
plt.show(fig)
