import random

def selection_sort(target: list):
    i = 0
    while i < len(target):
        j = i + 1
        while j < len(target):
            if target[i] > target[j]:
                target[j] , target[i] = target[i], target[j]
            j += 1
        i += 1
    
    return target

def merge_sort(target: list):
    if len(target) == 1:
        return target
    left = target[:int(len(target)/2)]
    right = target[int(len(target)/2):]
    left = merge_sort(left)
    right = merge_sort(right)
    i = 0
    j = 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        elif left[i] > right[j]:
            result.append(right[j])
            j += 1
        else:
            result.append(left[i])
            result.append(right[j])
            i += 1
            j += 1

    if i < len(left):
        result += left[i:]
    elif j < len(right):
        result += right[j:]

    return result

def quick_sort(target: list):
    if len(target) == 1:
        return target
    pivot = random.randint(0,len(target))
    left = target[:pivot]
    right = target[pivot:]
    left = merge_sort(left)
    right = merge_sort(right)
    i = 0
    j = 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        elif left[i] > right[j]:
            result.append(right[j])
            j += 1
        else:
            result.append(left[i])
            result.append(right[j])
            i += 1
            j += 1

    if i < len(left):
        result += left[i:]
    elif j < len(right):
        result += right[j:]

    return result

def counting_sort(target): # Assume the elements of the target are non-negative integers.
    max = 0
    counting_table = dict()
    result = []
    for i in target:
        if i > max:
            max = i
    for  i in range(max+1):
        counting_table[i] = 0
    for i in target:
        counting_table[i] += 1
    
    for i in range(max+1):
        dup = counting_table[i]
        for _ in range(dup):
            result.append(i)
        
    return result



if __name__ == '__main__':
    test = [6, 252, 1, 3, 53, 5, 5, 2424, 2, 1, 3]
    print(test)
    print(selection_sort(test))
    print(merge_sort(test))
    print(quick_sort(test))
    print(counting_sort(test))