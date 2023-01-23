def remove_smallest(numbers):
    a = numbers[:]
    if a:
        a.remove(min(a))
    
    return print(a) 


remove_smallest([1, 2, 3, 4, 5])
