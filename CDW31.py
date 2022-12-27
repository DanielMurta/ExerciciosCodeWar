def nb_year(p0, percent, aug, p):
    year = 0
    temp = p0
    while temp < p:
        temp = int(temp * (percent / 100 + 1) + aug)
        year += 1
    return year

print(nb_year(1500, 5, 100, 5000))

# if p0 < p:
#        return nb_year(p0 + int(p0 * percent / 100) + aug, percent, aug, p, years + 1)
#    return years