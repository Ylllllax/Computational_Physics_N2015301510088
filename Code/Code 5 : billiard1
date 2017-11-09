import numpy as np
import matplotlib.pyplot as plt

class BILLIARD(object):
    def __init__(self):
        self.dt, self.time=0.001, 300
        self.n=int(self.time/self.dt)
        self.x, self.y, self.vx, self.vy = [0.2], [0], [1], [0.423]
    def calculate(self):
        for i in range(self.n):
            self.nextx = self.x[-1]+self.vx[-1]*self.dt
            self.nexty = self.y[-1]+self.vy[-1]*self.dt
            self.nextvx, self.nextvy = self.vx[-1], self.vy[-1]
            if self.nextx>1.0:
                self.nextx = 2-self.nextx
                self.nextvx = -self.nextvx
            elif self.nextx<-1.0:
                self.nextx = -2-self.nextx
                self.nextvx = -self.nextvx
            elif self.nexty>1.0:
                self.nexty = 2-self.nexty
                self.nextvy = -self.nextvy
            elif self.nexty<-1.0:
                self.nexty = -2-self.nexty
                self.nextvy = -self.nextvy
            else:
                self.nextvx, self.nextvy= self.nextvx, self.nextvy
                self.nextx,self.nexty=self.nextx, self.nexty
            
            self.x.append(self.nextx)
            self.y.append(self.nexty)
            self.vx.append(self.nextvx)
            self.vy.append(self.nextvy)
            
    def plot_position(self,_ax):   
        _ax.plot(self.x,self.y,':b')
    def plot_phase(self,_ax):   
        self.phase_x, self.phase_vx = [], []
        for i in range(len(self.x)):
            if abs(self.y[i]-0.)<4E-3 :
                self.phase_x.append(self.x[i])
                self.phase_vx.append(self.vx[i])
        _ax.plot(self.phase_x,self.phase_vx,'ob',markersize=2)
    
fig= plt.figure(figsize=(14,7))
ax1=plt.subplot(121)
ax2=plt.subplot(122)
    
comp=BILLIARD()
comp.calculate()
comp.plot_position(ax1)
comp.plot_phase(ax2)


ax1.set_xlim(-1.0,1.0)
ax2.set_xlim(-1.01,1.01)
ax1.set_ylim(-1.0,1.0)
ax2.set_ylim(-1.01,1.01)
ax1.set_xlabel(r'$x (m)$',fontsize=14)
ax1.set_ylabel(r'$y (m)$',fontsize=14)
ax1.set_title('Rectangular stadium - trajectory',fontsize=14)
ax2.set_xlabel(r'$x (m)$',fontsize=14)
ax2.set_ylabel(r'$v_x (m/s)$',fontsize=14)
ax2.set_title('Rectangular stadium - phase space plot',fontsize=14)

plt.show()
