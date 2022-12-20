def open_or_senior(data):
    list = []
    for c in data:
        if c[0] > 54 and c[1] > 7:
            list.append('Senior')
        else:
            list.append('Open')  

    return list          

open_or_senior([[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]])

# return ["Senior" if age >= 55 and handicap >= 8 else "Open" for (age, handicap) in data]