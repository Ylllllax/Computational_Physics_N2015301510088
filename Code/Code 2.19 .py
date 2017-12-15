import math
import numpy as np
import matplotlib.pyplot as pl
import mpl_toolkits.mplot3d 



def ball1(angle):
    
    t=[]
    t.append(0)
    dt=0.01
    y_0=1*10**4
    g=9.8
    omega=33
    S_0_m=4.1E-4
    end_time = 200

    angle1=angle*math.pi/180
    x=[]
    v_x=[]
    y=[]
    v_y=[]
    z=[]
    v_z=[]
    x.append(0)
    y.append(1.8)
    z.append(0)
    v_x.append(49*math.cos(angle1))
    v_y.append(49*math.sin(angle1))
    v_z.append(0)
    for i in range(int(end_time/dt)):
        B_2_m= 0.0039+ 0.0058/(1.+math.exp((((v_x[i]**2+v_y[i]**2+v_z[i]**2)**0.5)-35)/5))
        m=x[i]+v_x[i]*dt
        x.append(m)
        n=v_x[i]-B_2_m*((v_x[i]**2+v_y[i]**2+v_z[i]**2)**0.5)*v_x[i]*dt
        v_x.append(n)
        o=y[i]+v_y[i]*dt	
        y.append(o)
        p=v_y[i]-g*dt
        v_y.append(p)
        q=z[i]+v_z[i]*dt
        z.append(q)
        r=v_z[i]-(S_0_m*v_x[i]*omega)*dt
        v_z.append(r)
        if o <= 0 :
            break
    pl.plot(x,y,label=" %s $^\circ$" %angle)


pl.figure(figsize=(10,6))
angle=[]
for i in range(6):
    a=(35+i*5)
    angle.append(a)
    ball1(angle[i])
pl.xlabel("x(m)")
pl.ylabel("y(m)")
pl.legend()
pl.title('y-x with different angles')
pl.show()


def ball2(angle):
    
    t=[]
    t.append(0)
    dt=0.01
    y_0=1*10**4
    g=9.8
    omega=33
    S_0_m=4.1E-4
    end_time = 200

    angle1=angle*math.pi/180
    x=[]
    v_x=[]
    y=[]
    v_y=[]
    z=[]
    v_z=[]
    x.append(0)
    y.append(1.8)
    z.append(0)
    v_x.append(49*math.cos(angle1))
    v_y.append(49*math.sin(angle1))
    v_z.append(0)
    for i in range(int(end_time/dt)):
        B_2_m= 0.0039+ 0.0058/(1.+math.exp((((v_x[i]**2+v_y[i]**2+v_z[i]**2)**0.5)-35)/5))
        m=x[i]+v_x[i]*dt
        x.append(m)
        n=v_x[i]-B_2_m*((v_x[i]**2+v_y[i]**2+v_z[i]**2)**0.5)*v_x[i]*dt
        v_x.append(n)
        o=y[i]+v_y[i]*dt	
        y.append(o)
        p=v_y[i]-g*dt
        v_y.append(p)
        q=z[i]+v_z[i]*dt
        z.append(q)
        r=v_z[i]-(S_0_m*v_x[i]*omega)*dt
        v_z.append(r)
        if o <= 0 :
            break
    pl.plot(x,z,label=" %s $^\circ$" %angle)


pl.figure(figsize=(10,6))
angle=[]
for i in range(6):
    a=(35+i*5)
    angle.append(a)
    ball2(angle[i])
pl.xlabel("x(m)")
pl.ylabel("z(m)")
pl.legend()
pl.title('z-x with different angles')
pl.show()


def ball3(omega):
    
    t=[]
    t.append(0)
    dt=0.01
    y_0=1*10**4
    g=9.8
    angle=45
    S_0_m=4.1E-4
    end_time = 200

    angle1=angle*math.pi/180
    x=[]
    v_x=[]
    y=[]
    v_y=[]
    z=[]
    v_z=[]
    x.append(0)
    y.append(1.8)
    z.append(0)
    v_x.append(49*math.cos(angle1))
    v_y.append(49*math.sin(angle1))
    v_z.append(0)
    for i in range(int(end_time/dt)):
        B_2_m= 0.0039+ 0.0058/(1.+math.exp((((v_x[i]**2+v_y[i]**2+v_z[i]**2)**0.5)-35)/5))
        m=x[i]+v_x[i]*dt
        x.append(m)
        n=v_x[i]-B_2_m*((v_x[i]**2+v_y[i]**2+v_z[i]**2)**0.5)*v_x[i]*dt
        v_x.append(n)
        o=y[i]+v_y[i]*dt	
        y.append(o)
        p=v_y[i]-g*dt
        v_y.append(p)
        q=z[i]+v_z[i]*dt
        z.append(q)
        r=v_z[i]-(S_0_m*v_x[i]*omega)*dt
        v_z.append(r)
        if o <= 0 :
            break
    pl.plot(z,x,y,label=" %s $^\circ$" %omega)


fig= pl.figure(figsize=(20,8))
ax = pl.subplot(1,1,1,projection='3d')
omega=[]
for i in range(11):
    a=(-500+i*100)
    omega.append(a)
    ball3(omega[i])
ax.set_xlabel('z (m)', fontsize=18)
ax.set_ylabel('x (m)', fontsize=18)
ax.set_zlabel('y (m)', fontsize=18)
ax.set_title('Sidearm curve ball with different omega', fontsize=18)
ax.set_xlim(-150,150)
ax.set_ylim(0,150)
ax.set_zlim(0,100)
pl.show(fig)
