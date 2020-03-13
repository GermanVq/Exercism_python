import math 
def score(x, y):
    lands = math.sqrt(x**2+y**2)
    
    if lands <= 1:
        return 10
    elif lands <= 5:
        return 5
    elif lands <= 10:
        return 1
    else:
        return 0
    
        