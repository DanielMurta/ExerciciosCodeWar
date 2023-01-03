def abbrev_name(name):
    list = [c for c in name.split()]
    return list[0][0].capitalize() + '.' + list[1][0].capitalize()

print(abbrev_name('daniel murta'))