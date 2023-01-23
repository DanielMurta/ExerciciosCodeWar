def duplicate_encode(word):
    new_word = ''
    for letra in word.lower():
        if word.lower().count(letra) == 1:
            new_word += '('
        else:
            new_word += ')'

    return new_word
    
print(duplicate_encode('Success'))
#  return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])