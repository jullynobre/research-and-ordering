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
        n = randint(1, size)
        list.append(n)
        size -= 1
    return list


def shell_sort(array):
    n = len(array)
    gap = n//2
 
    while gap > 0:
        for i in range(gap, n):
            aux = array[i]
            j = i
            while  j >= gap and array[j-gap] > aux:
                array[j] = array[j-gap]
                j -= gap
            array[j] = aux
        gap //= 2
 

size = [1000, 20000, 40000, 60000, 80000, 100000]
time = []

for s in size:
    time.append(timeit.timeit("shell_sort({})".format(generateList(s)), setup="from __main__ import shell_sort", number=1))
    print(s)

desenhaGrafico(size, time, "Numbers", "Time")