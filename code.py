import random

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def func(x):
    f = 3*x - 2*x**2
    return f

a = -1
b = 2
n = 100
equipment = "random" #right/left/middle/random

segment = np.arange(a, b, (b-a)/n)
segment = list(segment)
if float(b) not in segment:
    segment.append(float(b))

x = []
if equipment == "right":
    x = [segment[i] for i in range(1, len(segment))]
elif equipment == "left":
    x = [segment[i] for i in range(len(segment)-1)]
elif equipment == "middle":
    for i in range(len(segment)-1):
        x.append(segment[i]+((segment[i+1]-segment[i])/2))
elif equipment == "random":
    for i in range(len(segment)-1):
        x.append(random.uniform(segment[i], segment[i+1]))

sum = 0
y = [func(i) for i in x]
fig,ax = plt.subplots()
ax.plot(x,y)

for i in range(len(x)):
    sum += y[i]*((b-a)/n)
    ax.add_patch(Rectangle((x[i], 0), ((b-a)/n), y[i],edgecolor='black',facecolor='None', lw = 1))


print(sum)

plt.show()
