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

def bubble_sort(array):
    size = len(array)
    isOrdenered = False

    while not isOrdenered:
        isOrdenered = True
        for i in range(0, size - 2):
            if array[i] < array [i + 1]:
                swap(array, i, i + 1)
                isOrdenered = False
        size -= 1

def swap(array, n1, n2):
    temp = array[n1]
    array[n1] = n2
    array[n2] = temp
    
size = [1000, 20000, 40000, 60000, 80000, 100000]
time = []

for s in size:
    time.append(timeit.timeit("bubble_sort({})".format(generate_decreasing_list(s)), setup="from __main__ import bubble_sort", number=1))
    print(s)

desenhaGrafico(size, time, "Numbers", "Time")
