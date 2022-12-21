def is_isogram(string):
    for i in string:
        return False if string.count(i) > 1 else True

print(is_isogram('aba'))