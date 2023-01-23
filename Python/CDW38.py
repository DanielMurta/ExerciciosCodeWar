def reverse_words(text):
    i = text[::-1]
    lista = i.split(' ')
    return " ".join(lista[::-1])
    
print(reverse_words('This is an example!'))

# return ' '.join(s[::-1] for s in str.split(' '))