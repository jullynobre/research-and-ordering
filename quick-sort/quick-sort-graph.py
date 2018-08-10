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

def generate_decreasing_list(size):
    list = []
    for i in range(0, size):
        list.append(i)
    return list

def swap(array, n1, n2):
    temp = array[n1]
    array[n1] = array[n2]
    array[n2] = temp

def partition(array, lo, hi):
    pivot = array[hi]
    i = lo - 1

    for j in range(lo, hi):
        if array[j] <= pivot:
            i += 1
            swap(array, i, j)
    swap(array, i + 1, hi)
    return i + 1

def quicksort(array, lo, hi):
    if lo < hi:
        p = partition(array, lo, hi)
        quicksort(array, lo, p - 1)
        quicksort(array, p + 1, hi)

size = [1000, 20000, 40000, 60000, 80000, 100000]
time = []

for s in size:
    time.append(timeit.timeit("quicksort({}, {}, {})".format(generateList(s), 0, s - 1), setup="from __main__ import quicksort", number=1))
    print(s)

desenhaGrafico(size, time, "Numbers", "Time")
