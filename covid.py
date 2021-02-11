import pandas as pd
import numpy as np
data = pd.read_csv("covid2.csv")
data2 = data.iloc[27871:28246,:]
data2.replace(np.nan,0)
cases = []
days = []
index = 1
for i in data2["total_cases"]:
    cases.append(i)
    days.append(index)
    index += 1
import matplotlib.animation as animation
from matplotlib import style
import matplotlib.pyplot as plt
import time
def data_gen(t=1):
    cnt = 0
    while cnt < 374:
        cnt += 1
        t += 1
        yield t,cases[t]
def init():
    ax.set_ylim(0,10)
    ax.set_xlim(0,10)
    del xdata[:]
    del ydata[:]
    line.set_data(xdata,ydata)

fig,ax = plt.subplots()
line, = ax.plot([],[],lw=1)
ax.grid()
xdata,ydata = [],[]

def run(data):
    t,y = data
    xdata.append(t)
    ydata.append(y)
    xmin,xmax = ax.get_xlim()
    ymin,ymax = ax.get_ylim()

    if t >= xmax:
        ax.set_xlim(xmin,xmax+5)
        ax.figure.canvas.draw()
    #line.set_data(xdata,ydata)

    if y >= ymax:
        ax.set_ylim(ymin,ymax*(1.5))
        ax.set_xlim(xmin,xmax+1)
    #line.set_data(xdata,ydata)
    line.set_data(xdata,ydata)
    return line

ani = animation.FuncAnimation(fig,run,data_gen,blit=False,interval=200,repeat=False,init_func=init)
plt.title("INDIA days vs cases")
plt.xlabel("days")
plt.ylabel("total +ve")
plt.show()