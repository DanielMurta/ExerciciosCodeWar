def digitize(n):
    n = str(n)
    n = n.replace('', ',')
    list = n.split(',')
    list.remove(list[0])
    list.pop()
    list2 = [int(c) for c in list]
    return list2[::-1]

    
digitize(35231)

# return [int(x) for x in str(n)[::-1]]