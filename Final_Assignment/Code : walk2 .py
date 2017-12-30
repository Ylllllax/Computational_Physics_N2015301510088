import numpy as np
import matplotlib.pyplot as plt

steps = np.linspace(0, 100, 101)
x_y0 = np.zeros(101)
x_now = np.zeros(500)
x2_now = np.zeros(500)
x_ave = np.zeros(101)
x2_ave = np.zeros(101)
'''
for i in range(100):
    for j in range(500):
        ruler = np.random.rand()
        if ruler<=0.5:
            x_now[j] = x_now[j] + 1
        else:
            x_now[j] = x_now[j] - 1
        x2_now[j] = x_now[j]**2
    average = sum(x_now)/500
    average2 = sum(x2_now)/500
    x_ave[i+1] = average
    x2_ave[i+1] = average2
'''
for i in range(100):
    for j in range(500):
        ruler = np.random.rand()
        if ruler<=0.5:
            a = np.random.rand()
            x_now[j] = x_now[j] + a
        else:
            b = np.random.rand()
            x_now[j] = x_now[j] - b
        x2_now[j] = x_now[j]**2
    average = sum(x_now)/500
    average2 = sum(x2_now)/500
    x_ave[i+1] = average
    x2_ave[i+1] = average2    

fig= plt.figure(figsize=(14,7))
ax1=plt.subplot(121)
ax2=plt.subplot(122)

ax1.scatter(steps, x_ave)
ax1.plot(steps, x_y0,'--b')
ax1.set_xlim(0,100)
ax1.set_ylim(-1,1)
ax1.grid(True)
ax1.set_xlabel('step number')
ax1.set_ylabel('x')
ax1.set_title('Random walk in one dimension')

para = np.polyfit(steps, x2_ave,1)
poly = np.poly1d(para)
y_fit = poly(steps)
ax2.scatter(steps, x2_ave,s=2)
ax2.plot(steps, y_fit, 'b')
ax2.set_xlim(0,100)
ax2.set_ylim(0,40)
ax2.grid(True)
ax2.set_xlabel('step number(= time)')
ax2.set_ylabel('<x^2>')
ax2.set_title('Random walk in one dimension')

plt.show()
