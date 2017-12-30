import numpy as np
import matplotlib.pyplot as plt

steps = np.linspace(0, 100, 101)
x_y0 = np.zeros(101)
x_now = np.zeros(101)


for i in range(100):
        ruler = np.random.rand()
        if ruler<=0.5:
            x_now[i+1] = x_now[i] + 1
        else:
            x_now[i+1] = x_now[i] - 1
    

fig= plt.figure(figsize=(10,10))

plt.scatter(steps, x_now)
plt.plot(steps, x_y0,'--b')
plt.xlim(0,100)

plt.grid(True)
plt.xlabel('step number')
plt.ylabel('x')
plt.title('Random walk in one dimension')
plt.show()
