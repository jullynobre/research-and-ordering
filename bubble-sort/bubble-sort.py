def bubble_sort(array):
    size = len(array)
    isOrdenered = False

    while not isOrdenered:
        isOrdenered = True
        for i in range(0, size - 2):
            if array[i] > array [i + 1]:
                swap(array, i, i + 1)
                isOrdenered = False
        size -= 1

def swap(array, n1, n2):
    temp = array[n1]
    array[n1] = n2
    array[n2] = temp
    
array = [5, 1, 7, 2, 8, 3]
bubble_sort(array)
print(array)