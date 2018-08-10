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

array = [1, 1, 1, 1, 1, 1]
quicksort(array, 0, len(array)-1)
print(array)