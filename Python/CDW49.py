def square_sum(numbers):
    #total = 0
    #for c in numbers:
    #    total += c**2

    return sum([c ** 2 for c in numbers])


print(square_sum([1,2]))
print(square_sum([0, 3, 4, 5]))
print(square_sum([]))
print(square_sum([-1,-2]))
print(square_sum([-1,0,1]))