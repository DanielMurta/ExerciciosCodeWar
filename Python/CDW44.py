def stray(arr):
    for numero in arr:
        if arr.count(numero) == 1:
            return numero

print(stray([2, 3, 2, 2, 2]))
print(stray([3, 2, 2, 2, 2]))
print(stray([1, 1, 1, 1, 1, 1, 2]))