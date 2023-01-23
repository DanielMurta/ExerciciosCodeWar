def series_sum(n):
    if n == 0:
        return "0.00"
    i = 4
    sum = 1
    for y in range(n - 1):
        sum += 1/i
        i += 3
    r = f'{sum:.2f}'
    return str(r)

print(series_sum(0))

#def series_sum(n):
#    return '{:.2f}'.format(sum(1.0/(3 * i + 1) for i in range(n)))

