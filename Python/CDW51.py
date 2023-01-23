def remove_char(s):
    lista = []
    for letra in s:
        lista.append(letra)

    lista.pop()
    lista.remove(lista[0])
    return ''.join(lista)



print(remove_char('chair'))
print(remove_char('book'))
print(remove_char('people'))
print(remove_char('place'))
print(remove_char('ok'))


# s[1 : -1]
