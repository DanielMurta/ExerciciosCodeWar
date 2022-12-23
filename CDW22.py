def is_square(n):
    r = n**(1/2)
    if n < 0:
        return False
    return True if r == int(r) else False



print(is_square(25))

#import math
#def is_square(n):
#    return n > -1 and math.sqrt(n) % 1 == 0;
    