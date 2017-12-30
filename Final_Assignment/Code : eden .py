import numpy as np
import matplotlib.pyplot as plt

x_now = np.zeros(5001)
y_now = np.zeros(5001)


for i in range(2000):
    j=i;
    while(j>=0):
        ruler = np.random.rand()
        if ruler<=0.25:
            x_now[j+1] = x_now[j] + 1
            y_now[j+1] = y_now[j]
        elif ruler>0.25 and ruler<=0.5:
            x_now[j+1] = x_now[j] - 1
            y_now[j+1] = y_now[j]
        elif ruler>0.5 and ruler<=0.75:
            y_now[j+1] = y_now[j] + 1
            x_now[j+1] = x_now[j]
        else:
            y_now[j+1] = y_now[j] - 1
            x_now[j+1] = x_now[j]
        if x_now[j+1]>40 or x_now[j+1]<-40 or y_now[j+1]>40 or y_now[j+1]<-40:
            x_now[j+1] = 0
            y_now[j+1] = 0
        j=j-1
        print(j)

fig= plt.figure(figsize=(10,10))

plt.scatter(x_now , y_now, marker='.')
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Eden Cluster')
plt.show()
