def grow(arr):
    total = 1
    for numero in arr:
        total *= numero
    
    return total

grow([1, 2, 3])
grow([4, 1, 1, 1, 4])
grow([2, 2, 2, 2, 2, 2])