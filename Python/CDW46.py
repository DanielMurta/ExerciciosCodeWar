def expanded_form(num):
    n = str(num)
    st = ''
    comprimento = len(n)
    for i, unidade in enumerate(n):
        if unidade != '0':
            st += ' + ' + unidade + str(int(comprimento - 1)) * '0', end='')
            comprimento -= 1
        if unidade == '0':
            comprimento -= 1
    return st.strip(' +')

    

expanded_form(12)
print()
expanded_form(42)
print()
expanded_form(70304)