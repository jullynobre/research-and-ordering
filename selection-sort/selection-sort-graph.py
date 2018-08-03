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
    while size > 0: 
        list.append(size)
        size -= 1
    return list

def swap(array, n1, n2):
    temp = array[n1]
    array[n1] = array[n2]
    array[n2] = temp

def selection_sort(array):
    i = 0
    j = 0
    for j in range(0, len(array) - 1):
        minimum = j
        for i in range(j + 1, len(array)):
            if array[i] < array[minimum]:
                minimum = i
        if minimum != j:
            swap(array, j, minimum)
    return array

size = [1000, 20000, 40000, 60000, 80000, 100000]
time = []

for s in size:
    time.append(timeit.timeit("selection_sort({})".format(generateList(s)), setup="from __main__ import selection_sort", number=1))
    print(s)

desenhaGrafico(size, time, "Numbers", "Time")
