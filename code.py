import random

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def func(x):
    f = 3*x - 2*x**2 #функция
    return f

a = -1 #начало отрезка
b = 2 #конец отрезка
print("Введите число разбиений")
n = int(input()) #число разбиений
print("Введите оснащение (right/left/middle/random)")
equipment = str(input()) #right/left/middle/random (оснащение)

segment = np.arange(a, b, (b-a)/n)
segment = list(segment)             #отрезок интегрирования
if float(b) not in segment:
    segment.append(float(b))

x = []#оснащение
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

sum = 0#сумма
y = [func(i) for i in x]
fig,ax = plt.subplots()
ax.plot(x,y) #выводим функцию

for i in range(len(x)):
    sum += y[i]*((b-a)/n)#считаем сумму
    ax.add_patch(Rectangle((x[i], 0), ((b-a)/n), y[i],edgecolor='black',facecolor='None', lw = 1)) #выводим нужный прямоугольник на экран


print(sum)#печатаем значение суммы

plt.show()
