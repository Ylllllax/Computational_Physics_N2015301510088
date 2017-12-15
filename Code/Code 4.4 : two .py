import numpy as np
import matplotlib.pyplot as plt

class TWO(object):
    def __init__(self):
        self.dt, self.time=0.002, 10
        self.n=int(self.time/self.dt)
        self.x, self.y, self.vx, self.vy = [1], [0], [0], [2*np.pi]
    def calculate(self):
        for i in range(self.n):
            self.r=np.sqrt(self.x[-1]**2+self.y[-1]**2)
            self.vx.append(self.vx[-1]-self.dt*(4*(np.pi**2)*self.x[-1]/self.r**3))
            self.x.append(self.x[-1]+self.dt*self.vx[-1])
            self.vy.append(self.vy[-1]-self.dt*(4*(np.pi**2)*self.y[-1]/self.r**3))
            self.y.append(self.y[-1]+self.dt*self.vy[-1])
            
    def plot_trajectory(self,_ax):
        _ax.plot(self.x,self.y,'-b')
    
fig= plt.figure(figsize=(8,8))
ax1=plt.subplot(111)
    
comp=TWO()
comp.calculate()
comp.plot_trajectory(ax1)



ax1.set_xlim(-1.0,1.0)
ax1.set_ylim(-1.0,1.0)
ax1.set_xlabel(r'$x (AU)$',fontsize=14)
ax1.set_ylabel(r'$y (AU)$',fontsize=14)
ax1.set_title('Earth orbiting the aun',fontsize=14)
plt.show()
