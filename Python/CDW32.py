def number(lines):
    return [f'{i + 1}: ' + c for i, c in enumerate(lines)]

print(number(['a', 'b', 'c']))