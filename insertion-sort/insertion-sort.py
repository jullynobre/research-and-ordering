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

a = [7, 2, 9, 2, 5, 9]
print(insertion_sort(a))