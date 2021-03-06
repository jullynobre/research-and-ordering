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

print(merge_sort([6, 8, 2, 4, 0]))