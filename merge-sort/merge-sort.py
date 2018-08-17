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

def rest(array):
    new_array = []
    for i in range(1, len(array)):
        new_array += [array[i]]
    return new_array

def merge(left, right):
    result = []

    while left and right:
        if left[0] <= right[0]:
            result += [left[0]]
            left = rest(left)
        else:
            result += [right[0]]
            right = rest(right)

    while left:
        result += [left[0]]
        left = rest(left)
    
    while right:
        result += [right[0]]
        right = rest(right)

    return result
