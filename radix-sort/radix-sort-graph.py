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

def countingSort(arr, exp1):
    n = len(arr)
 
    output = [0] * (n)
    count = [0] * (10)
 
    for i in range(0, n):
        index = (arr[i]//exp1)
        count[ (index)%10 ] += 1

    for i in range(1,10):
        count[i] += count[i-1]

    i = n-1
    while i>=0:
        index = (arr[i]//exp1)
        output[ count[ (index)%10 ] - 1] = arr[i]
        count[ (index)%10 ] -= 1
        i -= 1

    i = 0
    for i in range(0,len(arr)):
        arr[i] = output[i]
 
def radixSort(arr):
    max1 = max(arr)

    exp = 1
    while max1/exp > 0:
        countingSort(arr,exp)
        exp *= 10
 

size = [1000, 20000, 40000, 60000, 80000, 100000]
time = []

for s in size:
    time.append(timeit.timeit("radixSort({})".format(generateList(s)), setup="from __main__ import radixSort", number=1))
    print(s)

desenhaGrafico(size, time, "Numbers", "Time")
