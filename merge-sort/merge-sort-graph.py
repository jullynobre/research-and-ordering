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

def merge_sort(array):
    size_array = len(array)

    if size_array <= 1:
        return array
    
    left = []
    right = []

    for i in range(0, size_array):
        if i < size_array/2:
            left += [array[i]]
        else:
            right += [array[i]]
    
    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    result = []

    while left and right:
        if left[0] <= right[0]:
            result += [left[0]]
            left.pop(0)
        else:
            result += [right[0]]
            right.pop(0)

    while left:
        result += [left[0]]
        left.pop(0)
    
    while right:
        result += [right[0]]
        right.pop(0)

    return result

size = [1000, 20000, 40000, 60000, 80000, 100000]
time = []

for s in size:
    time.append(timeit.timeit("merge_sort({})".format(generateList(s)), setup="from __main__ import merge_sort", number=1))
    print(s)

desenhaGrafico(size, time, "Numbers", "Time")
