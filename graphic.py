import matplotlib.pyplot as plt
from random import randint
import timeit

def desenhaGrafico(x,y,xl = "Entradas", yl = "Saídas"):
    plt.plot(x,y, label = "Melhor Tempo")
    plt.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.show()  

def generateList(size):
    list = []
    while size > 0:
        n = randint(1, size * 100000)
        if n not in list: 
            list.append(n)
            size -= 1
    return list

size = [100,1000,10000,20000,30000,40000,50000]
time = []

for s in size:
    time.append(timeit.timeit("generateList({})".format(s), setup="from __main__ import generateList", number=1))

desenhaGrafico(size, time, "Números", "Tempo")