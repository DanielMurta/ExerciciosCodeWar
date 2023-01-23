import math

def litres(time):
    return 0 if time == 0 else math.floor(time * 0.5)


# return time // 2