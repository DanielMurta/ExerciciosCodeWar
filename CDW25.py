def find_short(s):
    #list = s.split(' ')
    #list_numbers = []
    #for c in list:
    #    list_numbers.append(len(c))
    #return min(list_numbers)
    return min(len(c) for c in s.split())

find_short('i want to travel the world writing code one day')

# return min(len(x) for x in s.split())