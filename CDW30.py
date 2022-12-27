def is_valid_walk(walk):
    soma_ns = 0
    soma_we = 0
    for i in walk:
        if i == 'n':
            soma_ns += 1
        if i == 's':
            soma_ns -= 1
        if i == 'w':
            soma_we += 1
        if i == 'e':
            soma_we -= 1
    if len(walk) == 10 and soma_ns == soma_we == 0:
        return True
    else:
        return False

print(is_valid_walk(['n','n','n','s','n','s','n','s','n','s']))

# return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')