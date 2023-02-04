def xo(s):
    str = s.replace('', "-")
    list = str.split('-')
    n_o = 0
    n_x = 0
    for c in list:
        if c == 'x' or c == 'X':
            n_x += 1
        if c == 'o' or c == 'O':
            n_o += 1
    print(n_x)
    print(n_o)
    if n_o == n_x:
        return True
    else:
        return False


print(xo("ooOxxx"))


#s = s.lower()
#    return s.count('x') == s.count('o')