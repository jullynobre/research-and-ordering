def swap(array, n1, n2):
    temp = array[n1]
    array[n1] = array[n2]
    array[n2] = temp

def selection_sort(array):
    i = 0
    j = 0
    for j in range(0, len(array) - 1):
        minimum = j
        for i in range(j + 1, len(array)):
            if array[i] < array[minimum]:
                minimum = i
        if minimum != j:
            swap(array, j, minimum)
    return array

print(selection_sort([2, 6, 3, 9, 1, 5]))