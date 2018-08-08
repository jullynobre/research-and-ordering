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

def insertion_sort(array):
    i = 1
    while i < len(array):
        j = i
        while j > 0 and array[j-1] > array[j]:
            swap(array, j, j-1)
            j = j - 1
        i = i + 1
    return array

size = [1000, 2000, 4000, 6000, 8000, 10000]
time = []

for s in size:
    time.append(timeit.timeit("insertion_sort({})".format(generate_decreasing_list(s)), setup="from __main__ import insertion_sort", number=1))
    print(s)

desenhaGrafico(size, time, "Numbers", "Time")
