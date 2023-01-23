def wave(people):
    string = people
    string.replace(string[0], string[0].upper())
    
    return string
        
        


print(wave('hello'))