# Python program for implementation of Shell Sort
 
def shell_sort(arr):
    n = len(arr)
    gap = n//2
 
    while gap > 0:
        for i in range(gap, n):
            aux = arr[i]
            j = i
            while  j >= gap and arr[j-gap] > aux:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = aux
        gap //= 2
 
 
arr = [ 12, 34, 54, 2, 3]
shell_sort(arr)
print(arr)