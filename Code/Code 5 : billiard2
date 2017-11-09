import numpy as np
import matplotlib.pyplot as plt


class BILLIARD(object):
    def __init__(self,_alpha):
        self.alpha, self.r, self.dt, self.time= _alpha, 1.0, 0.001, 500
        self.n=int(self.time/self.dt)
        self.x, self.y, self.vx, self.vy = [0.2], [0], [0.6], [0.8]
    def calculate(self):
        for i in range(self.n):
            self.nextx = self.x[-1]+self.vx[-1]*self.dt
            self.nexty = self.y[-1]+self.vy[-1]*self.dt
            self.nextvx, self.nextvy = self.vx[-1], self.vy[-1]
            if (self.nexty>self.alpha*self.r and self.nextx**2+(self.nexty-self.alpha*self.r)**2>self.r**2) \
                    or (self.nexty<-self.alpha*self.r and self.nextx**2+(self.nexty+self.alpha*self.r)**2>self.r**2) \
                    or (self.nextx>self.r) \
                    or (self.nextx<-self.r):
                self.nextx=self.x[-1]
                self.nexty=self.y[-1]
                while not( \
                        (self.nexty>self.alpha*self.r and self.nextx**2+(self.nexty-self.alpha*self.r)**2>self.r**2) \
                        or (self.nexty<-self.alpha*self.r and self.nextx**2+(self.nexty+self.alpha*self.r)**2>self.r**2) \
                        or (self.nextx>self.r) \
                        or (self.nextx<-self.r)):
                    self.nextx=self.nextx+self.nextvx*self.dt/100
                    self.nexty=self.nexty+self.nextvy*self.dt/100
                if self.nexty>self.alpha*self.r:
                    self.v = np.array([self.nextvx,self.nextvy])
                    self.norm =  1/self.r*np.array([self.nextx, self.nexty-self.alpha*self.r])
                    self.v_perpendicular = np.dot(self.v, self.norm)*self.norm
                    self.v_parrallel = self.v-self.v_perpendicular
                    self.v_perpendicular= -self.v_perpendicular
                    self.nextvx, self.nextvy= (self.v_parrallel+self.v_perpendicular)[0],(self.v_parrallel+self.v_perpendicular)[1]
                elif self.nexty<-self.alpha*self.r:
                    self.v = np.array([self.nextvx,self.nextvy])
                    self.norm =  1/self.r*np.array([self.nextx, self.nexty+self.alpha*self.r])
                    self.v_perpendicular = np.dot(self.v, self.norm)*self.norm
                    self.v_parrallel = self.v-self.v_perpendicular
                    self.v_perpendicular= -self.v_perpendicular
                    self.nextvx, self.nextvy= (self.v_parrallel+self.v_perpendicular)[0],(self.v_parrallel+self.v_perpendicular)[1]
                else:
                    self.nextvx, self.nextvy= -self.nextvx, self.nextvy
            self.x.append(self.nextx)
            self.y.append(self.nexty)
            self.vx.append(self.nextvx)
            self.vy.append(self.nextvy)
    def plot_position(self,_ax):   
        _ax.plot(self.x,self.y,'-b')
        _ax.plot([self.r]*10,np.linspace(-self.alpha*self.r,self.alpha*self.r,10),'-k',lw=5)
        _ax.plot([-self.r]*10,np.linspace(-self.alpha*self.r,self.alpha*self.r,10),'-k',lw=5)
        _ax.plot(self.r*np.cos(np.linspace(0,np.pi,100)),self.r*np.sin(np.linspace(0,np.pi,100))+self.alpha*self.r,'-k',lw=5)
        _ax.plot(self.r*np.cos(np.linspace(np.pi,2*np.pi,100)),self.r*np.sin(np.linspace(np.pi,2*np.pi,100))-self.alpha*self.r,'-k',lw=5)
    def plot_phase(self,_ax):   
        self.phase_x, self.phase_vx = [], []
        for i in range(len(self.x)):
            if abs(self.y[i]-0.)<1E-3 :
                self.phase_x.append(self.x[i])
                self.phase_vx.append(self.vx[i])
        _ax.plot(self.phase_x,self.phase_vx,'ob',markersize=2)

fig= plt.figure(figsize=(14,7))
ax1=plt.subplot(121)
ax2=plt.subplot(122)

comp=BILLIARD(0)
comp.calculate()
comp.plot_position(ax1)
comp.plot_phase(ax2)


ax1.set_xlim(-1,1)
ax2.set_xlim(-1,1)
ax1.set_ylim(-1,1)
ax2.set_ylim(-1,1)
ax1.set_xlabel(r'$x (m)$',fontsize=14)
ax1.set_ylabel(r'$y (m)$',fontsize=14)
ax1.set_title('Circular stadium - trajectory',fontsize=14)
ax2.set_xlabel(r'$x (m)$',fontsize=14)
ax2.set_ylabel(r'$v_x (m/s)$',fontsize=14)
ax2.set_title('Circular stadium - phase space plot',fontsize=14)

plt.show()

'''
comp=BILLIARD(0.01)
comp.calculate()
comp.plot_position(ax1)
comp.plot_phase(ax2)

ax1.set_xlim(-1,1)
ax2.set_xlim(-1,1)
ax1.set_ylim(-1,1)
ax2.set_ylim(-1,1)
ax1.set_xlabel(r'$x (m)$',fontsize=14)
ax1.set_ylabel(r'$y (m)$',fontsize=14)
ax1.set_title('Stadium billiard'+r'$\alpha=0.01$'+': trajectory',fontsize=14)
ax2.set_xlabel(r'$x (m)$',fontsize=14)
ax2.set_ylabel(r'$v_x (m/s)$',fontsize=14)
ax2.set_title('Statium billiard: '+r'$\alpha=0.01$'+': phase-space',fontsize=14)

plt.show()
'''
