# Python program for implementation of Shell Sort
 
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
 
array = [43, 6, 8, 2, 0]
shell_sort(array)
print(array)