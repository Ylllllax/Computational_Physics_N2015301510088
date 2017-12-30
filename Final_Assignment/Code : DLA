import numpy as np
import matplotlib.pyplot as plt
import random

x_now = np.zeros(5001)
y_now = np.zeros(5001)
x_walk=0
y_walk=0
n=0

def stay(x,y,i):
    for j in range(i):
        if x==x_now[j]+1 and y==y_now[j]:
            return 1
            break
        elif x==x_now[j]-1 and y==y_now[j]:
            return 1
            break
        elif x==x_now[j] and y==y_now[j]+1:
            return 1
            break
        elif x==x_now[j] and y==y_now[j]-1:
            return 1
            break
    
def walk(x,y):
    ruler = np.random.rand()
    if ruler<=0.25:
        x = x + 1
        y = y
    elif ruler>0.25 and ruler<=0.5:
        x = x - 1
        y = y
    elif ruler>0.5 and ruler<=0.75:
        x = x
        y = y + 1
    else:
        x = x 
        y = y - 1
    return (x,y)

for n in range(1,1000): 
    m=0
    x_walk=random.randint(-30,30) 
    y_walk=random.randint(-30,30)
    while(m>=0):  
        if x_walk>50:
            x_walk=random.randint(-30,30) 
        elif x_walk<-50:
            x_walk=random.randint(-30,30) 
        elif y_walk>50:
            y_walk=random.randint(-30,30)
        elif y_walk<-50:
            y_walk=random.randint(-30,30)
        else:
            (x_walk,y_walk)=walk(x_walk,y_walk)
            m=m+1
            print(m,x_walk,y_walk)
            if stay(x_walk,y_walk,n) == 1:
                x_now[n+1]=x_walk
                y_now[n+1]=y_walk
                break
    print(n)
    
fig= plt.figure(figsize=(10,10))
plt.scatter(x_now , y_now, marker='.')
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')
plt.title('DLA Cluster')
plt.show()
