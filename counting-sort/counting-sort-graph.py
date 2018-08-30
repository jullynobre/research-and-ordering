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
        n = randint(1, 100)
        list.append(n)
        size -= 1
    return list

def generate_decreasing_list(size):
    list = []
    while size > 0: 
        list.append(size)
        size -= 1
    return list

def counting_sort(array, maxval):
    m = maxval + 1
    count = [0] * m               
    for a in array:
        count[a] += 1             
    i = 0
    for a in range(m):            
        for _ in range(count[a]): 
            array[i] = a
            i += 1
    return array

#print(counting_sort( [1, 4, 7, 2, 1, 3, 2, 1, 4, 4, 3, 2, 1], 8 ))

size = [1000, 20000, 40000, 60000, 80000, 100000]
time = []

for s in size:
    time.append(timeit.timeit("counting_sort({}, 100)".format(generateList(s)), setup="from __main__ import counting_sort", number=1))
    print(s)

desenhaGrafico(size, time, "Numbers", "Time")
