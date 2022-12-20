def high_and_low(numbers):
    numbers = [int(c) for c in numbers.split(' ')]
    print(numbers)
    return print(f"{max(numbers)} {min(numbers)}")


high_and_low('1 2 -3 4 5')

