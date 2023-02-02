def sum_two_smallest_numbers(numbers):
    lista = []
    for position, number in enumerate(numbers):
        if len(lista) == 2:
            my_set = set(lista)
            new_list = list(my_set)
            return sum(new_list)

        else:
            if number == min(numbers):
                lista.append(number)
                numbers.pop(position)

            





print(sum_two_smallest_numbers([19, 5, 42, 2, 77]))
print(sum_two_smallest_numbers([7, 15, 12, 18, 22]))
