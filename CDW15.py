def count_sheep(n):
    if n == 0:
        return ''
    list = []
    for i in range(n + 1):
        list.append(f'{i + 1} sheep...')
    list.pop()
    string_ = ''.join(list)
    print(string_)
    
count_sheep(2)

# return ''.join(f"{i} sheep..." for i in range(1,n+1))