def diulis_sort(array):
    size = len(array)
    ordenered_control = [0 for i in range(size)]
    while not all(array[i] <= array[i + 1] for i in range(size - 1)):
        i = 0
        while ordenered_control[i]:
            i += 1

        correct_index = sum(j < array[i] for j in array)

        if ordenered_control[correct_index]:
            correct_index += 1
            while array[correct_index] == array[correct_index - 1]:
                correct_index += 1
        
        array[i], array[correct_index] = array[correct_index], array[i]
        ordenered_control[correct_index] = 1

    return array

print(diulis_sort([6, 8, 9, 3, 5, 7, 1, 4, 5, 7]))



